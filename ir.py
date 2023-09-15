import RPi.GPIO as GPIO
import time

sensor = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)

print("IR Sensor Ready.....")
print(" ")

try: 
   while True:
        if GPIO.input(sensor):
            print("Object Detected")
        else:
            print("No Object Dectected")
        time.sleep(.5)

except KeyboardInterrupt:
    GPIO.cleanup()