import time
import RPi.GPIO as GPIO
import adafruit_dht
from time import sleep
import board
from digitalio import DigitalInOut
from adafruit_character_lcd.character_lcd import Character_LCD_Mono
import math

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
    
    # Calculate the feel-like temperature using the given table
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
    # Calculate the feel-like temperature using the specified formula
    Ta = temperature
    RH = humidity
    Tw = Ta * math.atan(0.151977 * (RH + 8.313659) ** 0.5) + math.atan(Ta + RH) - math.atan(RH - 1.67633) + 0.00391838 * (RH ** 1.5) * math.atan(0.023101 * RH) - 4.686035
    feel_like_temperature = -0.2442 + 0.55399 * Tw + 0.45535 * Ta - 0.0022 * Tw**2 + 0.00278 * Tw * Ta + 3.0
    return feel_like_temperature

while True:
    temperature = dhtDevice.temperature
    humidity = dhtDevice.humidity
    
    if humidity is not None and temperature is not None:
        lcd.message = "Temp={0:0.1f}C\nHumidity={1:0.1f}%".format(temperature, humidity)
        sleep(2)
        lcd.clear()
        
        if temperature >= 28:
            feel_like_temp = calculate_feel_like_temperature_above_28(temperature, humidity)
        else:
            feel_like_temp = calculate_feel_like_temperature_below_28(temperature, humidity)
        
        lcd.message = "Feel Like={0:0.1f}C".format(feel_like_temp)
        sleep(2)
    else:
        lcd.message = "Failed to get reading.\nTry again!"

    sleep(2)
    lcd.clear()