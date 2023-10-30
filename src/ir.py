import RPi.GPIO as GPIO
import time
from aws_connect import publishData

sensor = 16
speaker = 36

armed = True

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(speaker,GPIO.OUT)

print("IR Sensor Ready.....")
print(" ")

try: 
   while armed:
        if GPIO.input(sensor):
            print("Object Detected")
            publishData("IR Sensor")
            while fr_.run_recognition() == "Unknown":
                GPIO.output(speaker, 1)
            armed = False
        else:
            #GPIO.output(speaker, 0)
            print("No Object Detected")
        time.sleep(.5)

except KeyboardInterrupt:
    GPIO.cleanup()