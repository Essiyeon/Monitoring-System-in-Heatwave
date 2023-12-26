import cv2
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import time
import RPi.GPIO as GPIO

import busio
import board
import adafruit_amg88xx

import numpy as np

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

# 추가: GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT) #buzzer

while True:
    # read temperature
    pixels = amg.pixels
    max_temp = np.amax(pixels) + calib
    
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