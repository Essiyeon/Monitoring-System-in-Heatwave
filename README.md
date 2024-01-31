## Monitoring System for Worker Safety in Heatwave Season
혹서기 작업자의 안전을 위한 감독 시스템

### project (main directory)
디렉토리 구조 및 예시 사진

  - 1. Adafruit_CircuitPython_AMG88xx
    - examples
        * amg88xx_rpi_thermal_cam_console.py

        <img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/75f3994f-2dc7-46e3-aed6-16d04764b365" width="300" height="200"/>
        
        * amg88xx_simpletest.py

        <img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/731ca9a3-0288-4f4b-b307-9090bad1e8e7" width="300" height="200"/>
        
  - 2. Face_Detection_Camera
    * **all.py**
    * all_cv2.py
    * Face_detection_and_temperature_display.py
        
    <img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/6bfa5d24-4145-4faa-8d31-79c33342cb9e" width="300" height="250"/>
      
    * Face_detection_and_temperature_display-3.py
    
    <img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/03ff62da-4b83-46d5-8d92-1558e7d447eb" width="300" height="250"/>
    
  - 3. IRcam
    - AMG8833_IRcam
      - examples
        * IR_cam_interp.py
        
        <img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/fd901b24-15a5-4919-b8cd-17492b7fb010" width="300" height="200"/>
        
        * IR_cam_test.py

        <img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/af6dd2c0-a051-4555-bca7-e3fc3fa56cd9" width="300" height="200"/>
       
  - 4. examples
       * dht22_db.py
       * dht22_example.py
       * dht22_lcd.py
      
       <img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/bcb134c9-b672-4866-b7cd-569f94b27882" width="250" height="150"/>
       
       * dht22_lcd_led.py
       * flask_DHT22_LCD_LED-2.py
      
       <img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/d336cb79-3ac6-4089-abdf-0c95b432e7ae" width="250" height="500"/>
       
       * flask_DHT22_LCD_LED-3(DBX).py
       * flask_DHT22_LCD_LED-4(DBX)_cv2.py
       * flask_DHT22_LCD_LED-5(DBX)_haar.py
       * flask_DHT22_LCD_LED.py
       * haarcascade_frontalface_default.xml
       * lcd_example.py
      - templates
          * index00.html
        
          <img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/9b623c4c-1541-4cd9-9a7a-1e6c73ee360f" width="300" height="175"/>
          
          * index01.html
       
          <img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/ec8ed453-2caf-42dd-8ac0-6891f4a321be" width="450" height="200"/>
          
          * index02.html
          * index03.html

  - 5. face_detection
    * face_detection-1.py
    * face_detection-2.py
    
    <img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/04516ad8-3ee8-4bb2-879f-34e63fd0510a" width="300" height="250"/>
    
    * haarcascade_frontalface_default.xml
         
  - 6. opencv

  * blinka_exam.py
  * openCV_test.py

  <img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/143633ae-4025-497d-9326-93ae043f6a2a" width="300" height="175"/>
  
  * openCV_test0.py

  <img src="https://github.com/Essiyeon/Monitoring-System-in-Heatwave/assets/100012844/3a3c4c7f-0f78-4d44-be9b-e72bafb9b5a7" width="300" height="250"/>
  
  * openCV_test1.py

---
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

flask 웹 구현이전 발표이므로 해당부분 구현 사진이 빠져있음

2023.12.28 flask 까지 구현 완료

---
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
12.26|라즈베리파이-깃허브 연동 및 일괄 업로드|

---

레퍼런스 1 
[How to Build a Face Mask Detector with Raspberry Pi](https://www.tomshardware.com/how-to/raspberry-pi-face-mask-detector)

레퍼런스 2 
[How to Install TensorFlow 2 and OpenCV on a Raspberry Pi](https://www.youtube.com/watch?v=vekblEk6UPc)

레퍼런스 3
[How to Install OpenCV on a Raspberry Pi](https://www.youtube.com/watch?v=QzVYnG-WaM4)

레퍼런스 4
[RASPBERRY PI MASK DETECTION](https://courses.ece.cornell.edu/ece5990/ECE5725_Spring2022_Projects/Thursday%20May%2019/Pi%20Mask%20Detection/W_dsw247_tdt46_website/index.html)

레퍼런스 5
[Raspberry Pi Object Detection Tutorial](https://www.youtube.com/watch?v=NPXBRX7N3ec&t=7s)

레퍼런스 6
[열 화상 카메라 만들어 볼까요? (Adafruit AMG8833 IR Thermal Camera)](https://www.youtube.com/watch?v=rqdTx0AKroE)

레퍼런스 7
[openCV 안면 인식 Tutorial](https://velog.io/@cdspacenoob/kingrcelo)

레퍼런스 8
[실시간 얼굴인식(Face Recognition) with Raspberry Pi 3](https://jayharvey.tistory.com/4)

레퍼런스 9
[실시간 얼굴 인식 (2) openCV, haarcascades](https://sinawi.tistory.com/119)

레퍼런스 10
[Code_Interview](https://github.com/dungdo123/Code_Interview)

레퍼런스 11
[Build Face Detection with Python using OpenCV (With link to the code)](https://www.youtube.com/watch?v=n12PXImCWFo)

레퍼런스 12
[Haar Cascade Object Detection Face & Eye OpenCV Python Tutorial](https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/)

레퍼런스 13
[Thermal Camera Analysis with Raspberry Pi (AMG8833)](https://makersportal.com/blog/thermal-camera-analysis-with-raspberry-pi-amg8833)

레퍼런스 14
[Adafruit AMG8833 8x8 Thermal Camera Sensor](https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor)
[Adafruit AMG8833 8x8 Thermal Camera Sensor-Python & CircuitPython](https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor/python-circuitpython)

레퍼런스 15
[Using a 16x2 LCD Display with a Raspberry Pi](https://www.youtube.com/watch?v=cVdSc8VYVBM)
[LCD Display Tutorial for Raspberry Pi](https://www.rototron.info/lcd-display-tutorial-for-raspberry-pi/#cp)

레퍼런스 16
[openCV python#7 사람얼굴 인식하기](https://www.youtube.com/watch?v=hr7ghNicP8o)

레퍼런스 17
[[Computer Vision] AI는 어떻게 얼굴을 인식할까? 1탄 (Ft. Viola & Jones, Haar Cascade)](https://kay-dev.tistory.com/entry/Open-CV-Haar-Cascade%EC%99%80-%EC%96%BC%EA%B5%B4-%EC%9D%B8%EC%8B%9D-Ft-Viola-Jones)

레퍼런스 18
[OpenCV 강좌 - Haar Cascades에 대해 알아보자.](https://webnautes.tistory.com/1352)

레퍼런스 19
[haar cascade face detection 얼굴 검출](https://data-science.tistory.com/143)

레퍼런스 20
[[라즈베리파이 온습도계] DHT22 센서, 1602 LCD 패널 연결 및 테스트](https://blog.naver.com/PostView.naver?blogId=ts_stephan&logNo=222304187058&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView)

레퍼런스 21
[Python Thermal Camera with Raspberry Pi (AMG8833)](https://github.com/makerportal/AMG8833_IR_cam#--real-time-interpolated-ir-camera--)

레퍼런스 22
[라즈베리파이 수집센서값 Maria DB에 저장하고 화면에 보여주기](https://blog.naver.com/simjk98/221229266764)

레퍼런스 23
[라즈베리파이 온습도센서 값을 MariaDB에 저장하기](https://engine.tistory.com/57)

(오류 구글링 링크들은 제외했습니다.)
~~정말 많은 분들의 블로그와 유튜브 덕분에 공부할 수 있었습니다... 압도적 감사... 정말로... 감사합니다...~~




