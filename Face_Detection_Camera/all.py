import sys
import time
import RPi.GPIO as GPIO
import adafruit_dht
from time import sleep
import board
from digitalio import DigitalInOut
from adafruit_character_lcd.character_lcd import Character_LCD_Mono
import math
import pymysql

import cv2
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import busio
import adafruit_amg88xx
import numpy as np

conn=pymysql.connect(host="localhost",
                    user="raspi_user",
                    passwd="dsp502",
                    db="raspi_db")

# GPIO 핀 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)  # GPIO 21 Green LED
GPIO.setup(20, GPIO.OUT)  # GPIO 20 Yellow LED
GPIO.setup(16, GPIO.OUT)  # GPIO 16 Red LED
GPIO.setup(12, GPIO.OUT) #buzzer

dhtDevice = adafruit_dht.DHT22(board.D4)

lcd_columns = 16
lcd_rows = 2

lcd_rs = DigitalInOut(board.D26)
lcd_en = DigitalInOut(board.D19)
lcd_d4 = DigitalInOut(board.D13)
lcd_d5 = DigitalInOut(board.D6)
lcd_d6 = DigitalInOut(board.D5)
lcd_d7 = DigitalInOut(board.D11)

lcd = Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows
)

# init calib parameter for thermal sensor
calib = 7.5

# define classifier
classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

# start video stream
print("[INFO] starting video stream...")
vs = VideoStream(src=-1).start()
time.sleep(1)

fps = FPS().start()

def calculate_feel_like_temperature_above_28(temperature, humidity):
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
    Ta = temperature
    RH = humidity
    Tw = Ta * math.atan(0.151977 * (RH + 8.313659) ** 0.5) + math.atan(Ta + RH) - math.atan(RH - 1.67633)+ 0.00391838 * (RH ** 1.5) * math.atan(0.023101 * RH) - 4.686035
    feel_like_temperature = -0.2442 + 0.55399 * Tw + 0.45535 * Ta - 0.0022 * Tw**2 + 0.00278 * Tw * Ta + 3.0
    return feel_like_temperature


try:
    with conn.cursor() as cur : #커서객체 생성, 커서 객체에 DB작업을 위한 함수들이 포함되어 있기 때문에 생성
        sql="insert into temp_data values(%s, %s, %s, %s, %s, %s)"
            #각 자리에 문자열 하나씩
        while True:
            temperature = dhtDevice.temperature
            humidity = dhtDevice.humidity
            
            if humidity is not None and temperature is not None:
                lcd.message = "Temp={0:0.1f}C\nHumidity={1:0.1f}%".format(temperature, humidity)
                print("Temp={0:0.1f}C\nHumidity={1:0.1f}%".format(temperature, humidity))
                sleep(5)
                lcd.clear()
                
                if temperature >= 28:
                    feel_like_temp = calculate_feel_like_temperature_above_28(temperature, humidity)
                else:
                    feel_like_temp = calculate_feel_like_temperature_below_28(temperature, humidity)
                
                lcd.message = "Feel Like={0:0.1f}C".format(feel_like_temp)
                
                
                sleep(2)
               
                # 체감온도에 따라 LED 제어
                if feel_like_temp >= 38: 
                    GPIO.output(16, GPIO.HIGH) #Red LED
                    GPIO.output(21, GPIO.LOW)
                    GPIO.output(20, GPIO.LOW)
                elif feel_like_temp >= 35:
                    GPIO.output(20, GPIO.HIGH) #Yellow LED
                    GPIO.output(16, GPIO.LOW)
                    GPIO.output(21, GPIO.LOW)
                elif feel_like_temp >= 33:
                    GPIO.output(21, GPIO.HIGH) #Green LED
                    GPIO.output(16, GPIO.LOW)
                    GPIO.output(20, GPIO.LOW) 
                else:
                    GPIO.output(16, GPIO.LOW)
                    GPIO.output(20, GPIO.LOW)
                    GPIO.output(21, GPIO.LOW)
            else:
                lcd.message = "Failed to get reading.\nTry again!"

            sleep(2)
            lcd.clear()
            
            # read temperature
            pixels = amg.pixels
            max_temp = np.amax(pixels) + calib
            
            cur.execute(sql,
                        ('DHT22',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),
                        temperature, humidity, feel_like_temp, max_temp))
            conn.commit()
                
            # 영상 캡처
            frame = vs.read()
            
            # 파이카메라 영상을 그레이 스케일로 변환
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # notice distance
            cv2.putText(frame, "distance to camera: 20cm", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0))
            
            # face detection
            bboxes = classifier.detectMultiScale(gray_frame)  # 그레이 스케일 영상으로 얼굴 검출
            
            # print bounding box for each detected face
            for box in bboxes:
                x, y, width, height = box
                x2, y2 = x + width, y + height
                # draw rectangle over the pixels
                cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 2)
                text_pos = y - 15 if y - 15 > 15 else y + 15
                temp_text = str(max_temp)

                # 체온이 38도 이상이면 텍스트 색상을 빨간색으로 변경
                if max_temp >= 38:
                    cv2.putText(frame, temp_text + 'oC', (x, text_pos), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
                    GPIO.output(12, GPIO.HIGH) #Buzzer ON
                else:
                    cv2.putText(frame, temp_text + 'oC', (x, text_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0))
                    GPIO.output(12, GPIO.LOW) #Buzzer OFF

            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord("q"):
                break
            fps.update()
            
        fps.stop()
        cv2.destroyAllWindows()
        vs.stop()
        GPIO.cleanup()
except KeyboardInterrupt :
    exit()
finally :
    conn.close()
