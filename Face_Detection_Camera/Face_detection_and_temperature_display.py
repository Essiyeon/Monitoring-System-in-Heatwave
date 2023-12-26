import cv2
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import time

import busio
import board
import adafruit_amg88xx
#from Adafruit_AMG88xx import Adafruit_AMG88xx

import numpy as np

# init calib parameter for thermal sensor
calib = 7.5

# define classifier
classifier = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)
# init AMG8833 thermal sensor
#sensor = Adafruit_AMG88xx()

# start video stream
print("[INFO] starting video stream...")
vs = VideoStream(src=-1).start()
time.sleep(1)

fps = FPS().start()
while True:
    
    # read temperature
    #pixels = sensor.readPixels()
    pixels = amg.pixels
    
    max_temp = np.amax(pixels) + calib
    image = vs.read()
    # notice distance
    cv2.putText(image, "distance to camera: 40cm", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0))
    # face detection
    bboxes = classifier.detectMultiScale(image)
    
    # print bounding box for each detected face
    for box in bboxes:
      # extract
      x, y, width, height = box
      x2, y2 = x + width, y + height
      # draw rectangle over the pixels
      cv2.rectangle(image, (x, y), (x2, y2), (0,0,255), 2)
      text_pos = y - 15 if y - 15 >15 else y+ 15
      temp_text = str(max_temp)
      cv2.putText(image, temp_text + 'oC', (x, text_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0))
    
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):
        break
    fps.update()

fps.stop()
cv2.destroyAllWindows()
vs.stop()


    
    
