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
09.11|Github연동, JavaFX 라이브러리 설치, 한글깨짐 오류 해결|
09.12|JavaFX 모듈 설치 오류 해결|
09.15|주제 후보 설정 및 Jsoup 라이브러리 설치, 설치 오류 해결|
09.18|CGV영화 예매차트 크롤링코드 동작 확인 (콘솔창 출력),GUI창에 띄우도록 수정|
09.19|주제 확정, 구현기능 정리|
09.25|2nd Commit 뉴스의 헤드라인을 GUI 창에 출력, 3rd Commit GUI창의 기사 헤드라인 클릭 시 기사본문으로 이동하는 기능구현|
10.01|1st Commit 시스템에서 현재 날짜를 받아와서 실시간으로 기사를 출력하도록 프로그램 수정, 2nd Commit 새로고침 버튼 추가, 3rd Commit 버전업데이트시에 빠트린 코드 추가|
10.06|뉴스 이미지와 기사를 함께 출력하도록 업데이트|


