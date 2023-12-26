import cv2
from flask import Flask, render_template, Response
from flask_apscheduler import APScheduler
from flask import jsonify
import sys
import time
import RPi.GPIO as GPIO
import adafruit_dht
from time import sleep
import board
from digitalio import DigitalInOut
from adafruit_character_lcd.character_lcd import Character_LCD_Mono
import math
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import numpy as np

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)

# 초기 온도, 습도, 체감온도 값 설정
temperature = 0
humidity = 0
feel_like_temp = 0

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)  # GPIO 21 Green LED
GPIO.setup(20, GPIO.OUT)  # GPIO 20 Yellow LED
GPIO.setup(16, GPIO.OUT)  # GPIO 16 Red LED

# DHT22 센서 설정
dhtDevice = adafruit_dht.DHT22(board.D4)

# LCD 설정
lcd_columns = 16
lcd_rows = 2
lcd_rs = DigitalInOut(board.D26)
lcd_en = DigitalInOut(board.D19)
lcd_d4 = DigitalInOut(board.D13)
lcd_d5 = DigitalInOut(board.D6)
lcd_d6 = DigitalInOut(board.D5)
lcd_d7 = DigitalInOut(board.D11)
lcd = Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

# 영상 스트리밍을 위한 VideoStream 및 FPS 객체 생성
vs = VideoStream(src=0).start()
time.sleep(2.0)
fps = FPS().start()

def generate_frames():
    while True:
        # 프레임 읽기
        frame = vs.read()

        # 프레임을 바이트 스트림으로 인코딩
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        # 프레임 반환
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    global temperature, humidity, feel_like_temp
    return render_template('index03.html', temperature=temperature, humidity=humidity, feel_like_temp=feel_like_temp)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@scheduler.task("interval", id="update_lcd", seconds=15)
def update_lcd_task():
    global temperature, humidity, feel_like_temp
    with app.app_context():
        try:
            sleep(5)
            temperature = dhtDevice.temperature
            humidity = dhtDevice.humidity

            if humidity is not None and temperature is not None:
                # LCD에 온도, 습도, 체감온도 표시
                lcd.message = "Temp={0:0.1f}C\nHumidity={1:0.1f}%".format(temperature, humidity)
                sleep(5)
                lcd.clear()
                
                # 체감온도 계산 함수 호출
                if temperature >= 28:
                    feel_like_temp = calculate_feel_like_temperature_above_28(temperature, humidity)
                else:
                    feel_like_temp = calculate_feel_like_temperature_below_28(temperature, humidity)

                lcd.message = "Feel Like={0:0.1f}C".format(feel_like_temp)
                sleep(5)
                lcd.clear()

                # 체감온도에 따라 LED 제어
                control_led_based_on_feel_like_temperature(feel_like_temp)
                
            sleep(5)

        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print(f"An error occurred: {e}")

@app.route('/data')
def get_data():
    global temperature, humidity, feel_like_temp
    return jsonify({
        'temperature': temperature,
        'humidity': humidity,
        'feel_like_temp': feel_like_temp
    })

def calculate_feel_like_temperature_above_28(temperature, humidity):
    # 계산식을 사용하여 체감온도 계산
    feellike_temp_table = [
        [26.6, 27.6, 28.5, 29.5, 30.4, 31.4, 32.4, 33.3, 34.3, 35.3, 36.2, 37.2, 38.2],
        [27.1, 28.1, 29.0, 30.0, 31.0, 32.0, 32.9, 33.9, 34.9, 35.9, 36.9, 37.8, 38.8],
        [27.6, 28.6, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.4, 36.4, 37.4, 38.4, 39.4],
        [28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0],
        [28.4, 29.4, 30.4, 31.4, 32.4, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5],
        [28.9, 29.9, 30.9, 31.9, 32.9, 33.9, 34.9, 35.9, 36.9, 38.0, 39.0, 40.0, 41.0],
        [29.3, 30.3, 31.3, 32.3, 33.3, 34.3, 35.4, 36.4, 37.4, 38.4, 39.5, 40.5, 41.5],
        [29.7, 30.7, 31.7, 32.7, 33.7, 34.8, 35.8, 36.8, 37.8, 38.9, 39.9, 40.9, 42.0],
        [30.0, 31.1, 32.1, 33.1, 34.1, 35.2, 36.2, 37.2, 38.3, 39.3, 40.4, 41.4, 42.4],
        [30.4, 31.4, 32.5, 33.5, 34.5, 35.6, 36.6, 37.7, 38.7, 39.7, 40.8, 41.8, 42.9],
        [30.8, 31.8, 32.9, 33.9, 34.9, 36.0, 37.0, 38.1, 39.1, 40.2, 41.2, 42.3, 43.3]
    ]

    temp_index = int(round(temperature - 28))
    hum_index = int((humidity - 40) / 5)

    if temp_index < 0:
        temp_index = 0
    elif temp_index >= len(feellike_temp_table):
        temp_index = len(feellike_temp_table) - 1

    if hum_index < 0:
        hum_index = 0
    elif hum_index >= len(feellike_temp_table[0]):
        hum_index = len(feellike_temp_table[0]) - 1

    return feellike_temp_table[hum_index][temp_index]

def calculate_feel_like_temperature_below_28(temperature, humidity):
    # 계산식을 사용하여 체감온도 계산
    Ta = temperature
    RH = humidity
    Tw = Ta * math.atan(0.151977 * (RH + 8.313659) ** 0.5) + math.atan(Ta + RH) - math.atan(RH - 1.67633) + 0.00391838 * (RH ** 1.5) * math.atan(0.023101 * RH) - 4.686035
    feel_like_temperature = -0.2442 + 0.55399 * Tw + 0.45535 * Ta - 0.0022 * Tw**2 + 0.00278 * Tw * Ta + 3.0
    return feel_like_temperature

def control_led_based_on_feel_like_temperature(feel_like_temp):
    # 체감온도에 따라 LED 제어
    if feel_like_temp >= 38:
        GPIO.output(16, GPIO.HIGH)  # Red LED
        GPIO.output(21, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
    elif feel_like_temp >= 35:
        GPIO.output(20, GPIO.HIGH)  # Yellow LED
        GPIO.output(16, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
    elif feel_like_temp >= 33:
        GPIO.output(21, GPIO.HIGH)  # Green LED
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
    else:
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)

update_lcd_task()

if __name__ == '__main__':
    scheduler.start()
    app.run(host="192.168.0.54", port="8080")
