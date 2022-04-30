import RPi.GPIO as GPIO
import time
import os
 
SENSOR_PIN = 23
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

#Default timeout - turn off after 300ms
os.system("DISPLAY=:0 /usr/bin/xset dpms 300 0 0")
 
def my_callback(channel):
    # Turn display on
    os.system("DISPLAY=:0 /usr/bin/xset dpms force on")
try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=my_callback)
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print('Finish...')
GPIO.cleanup()
