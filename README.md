## Monitoring System for Worker Safety in Heatwave Season
혹서기 작업자의 안전을 위한 감독 시스템

### project (main directory)
  - 1. Adafruit_CircuitPython_AMG88xx
    - examples
        * amg88xx_rpi_thermal_cam_console.py
        * amg88xx_simpletest.py
        
  - 2. Face_Detection_Camera
    * **all.py**
    * all_cv2.py
    * Face_detection_and_temperature_display.py
    * Face_detection_and_temperature_display-3.py

  - 3. IRcam
    - AMG8833_IRcam
      - examples
        * IR_cam_interp.py
        * IR_cam_test.py
       
  - 4. examples
       * dht22_db.py
       * dht22_example.py
       * dht22_lcd.py
       * dht22_lcd_led.py
       * flask_DHT22_LCD_LED-2.py
       * flask_DHT22_LCD_LED-3(DBX).py
       * flask_DHT22_LCD_LED-4(DBX)_cv2.py
       * flask_DHT22_LCD_LED-5(DBX)_haar.py
       * flask_DHT22_LCD_LED.py
       * haarcascade_frontalface_default.xml
       * lcd_example.py
      - templates
          * index00.html
          * index01.html
          * index02.html
          * index03.html

  - 5. face_detection
    * face_detection-1.py
    * face_detection-2.py
    * haarcascade_frontalface_default.xml
         
  - 6. opencv

  * blinka_exam.py
  * openCV_test.py
  * openCV_test0.py
  * openCV_test1.py
    
### - all.py
< 혹서기 작업자의 안전을 위한 감독 시스템 >

2023.11.10 발표자료

<img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/254f9340-0a40-498b-9229-90e782c09217" width="600" height="350"/>
<img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/d0ea9bd3-ddd2-4462-8e5d-9adf1f3ba223" width="600" height="350"/>
<img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/e1134ce0-cfe0-4b1b-97b3-88519a4249e1" width="600" height="350"/>
<img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/b58cd56f-330f-4bfc-9a29-df36e056d8a0" width="600" height="350"/>
<img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/49dbc129-2033-4abf-8628-b372c990a275" width="600" height="350"/>
<img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/75dc1903-fe43-4cff-8fa6-99dd2c0c6d94" width="600" height="350"/>
<img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/0e3fb55a-fe3c-4e21-aae2-8e6407bea35f" width="600" height="350"/>
<img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/b7f0539a-eb1d-43f7-8f62-0d5041bf68ce" width="600" height="350"/>
<img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/15e63e8d-f681-4f62-9085-6dd8f5a7a7e7" width="600" height="350"/>
<img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/5d3f7193-7106-4863-a07c-a26cabcd10a7" width="600" height="350"/>
<img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/85fefe01-19c5-4d67-aa57-247fc0cfebf5" width="600" height="350"/>
<img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/604e7730-2307-457f-a51d-9ca10c605944" width="600" height="350"/>
<img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/d341a643-f6a5-4090-bef4-6d41062df895" width="600" height="350"/>
<img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/f434a94a-710d-4f75-b331-563e4bb023db" width="600" height="350"/>

flask 웹에 구현이전 발표이므로 해당부분 구현 사진이 빠져있음
2023.12.28 flask 까지 구현 완료



### - 구현과정

날짜|내용|
---|---|
08.07~08.08|DHT11, LM35 센서 활용, flask 웹 프레임워크 활용|
08.21~08.22|(레퍼런스1) Tensorflow, openCV install, 버전오류|
08.23|가상환경(virtualenv) 설정 및 설치 이어서|
08.24~08.27|설치 재시도 및 오류해결|
08.30~08.31|~~결국~~ 초기화, (레퍼런스2) 설치 다시 시도|
09.01|설치 완료 ~~드디어~~|
09.04~09.05|파이카메라 설정, (레퍼런스1)시도, OS에러해결|
09.06|코드수정, 오브젝트 디텍션 예제 확인|
09.07~09.10|DHT22센서 확인, 세븐세그먼트 출력 확인|
09.12~09.14|74HC595활용|
09.16~09.19|Haar cascade 활용 얼굴인식 및 열화상센서, LCD 주문|
10.10|중간 정리 및 AMG8833, LCD 납뗌, 예제 확인|
10.11~10.13|AMG8833센서 활용, 오류해결|
10.19|LCD예제 및 옵습도, 체감온도 출력 확인|
10.26~11.03|DHT22, LCD, FLASK, AMG8833, Picamera 등 전체 코드 합치기|
10.30~11.03|보고서 및 발표자료 만들기|
11.08~11.09|정확도 측정 및 mariaDB 추가|
11.10|발표(현재까지의 결과까지)|
11.30~12.07|flask 오류 해결, vnc 에러|
12.18|flask 오류 해결, 전체 완성|
12.26|라즈베리파이-깃허브 연동|


개발환경설정
레퍼런스 1 How to Build a Face Mask Detector with Raspberry Pi
레퍼런스 2 How to Install TensorFlow 2 and OpenCV on a Raspberry Pi

