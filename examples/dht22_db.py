import sys
import time
import board
import adafruit_dht
import pymysql

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4)

conn=pymysql.connect(host="localhost",
                    user="raspi_user",
                    passwd="dsp502",
                    db="raspi_db")

try:
    with conn.cursor() as cur : #커서객체 생성, 커서 객체에 DB작업을 위한 함수들이 포함되어 있기 때문에 생성
        sql="insert into temp_data values(%s, %s, %s, %s)"
            #각 자리에 문자열 하나씩
        while True:
            try:
                # Print the values to the serial port
                temperature_c = dhtDevice.temperature
                temperature_f = temperature_c * (9 / 5) + 32
                humidity = dhtDevice.humidity
                print(
                    "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                        temperature_f, temperature_c, humidity
                    )
                )
                cur.execute(sql,
                            ('DHT22',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),
                            temperature_c, humidity))
                conn.commit()


            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                print(error.args[0])
                time.sleep(2.0)
                continue
            except Exception as error:
                dhtDevice.exit()
                raise error

            time.sleep(2.0)
except KeyboardInterrupt :
    exit()
finally :
    conn.close()
