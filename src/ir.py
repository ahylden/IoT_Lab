import RPi.GPIO as GPIO
import time
from aws_connect import publishData

sensor = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)

print("IR Sensor Ready.....")
print(" ")

try: 
   while True:
        if GPIO.input(sensor):
            print("Object Detected")
            publishData("Object Detected")
        else:
            print("No Object Detected")
            #publishData("No Object Detected")
        time.sleep(.5)

except KeyboardInterrupt:
    GPIO.cleanup()