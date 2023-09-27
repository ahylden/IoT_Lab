import RPi.GPIO as GPIO
import signal
import sys
import time
from aws_connect import publishData

sensor = 16

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def ir_detection_callback(channel):
    print("Object Detected")
    publishData("IR Sensor")

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sensor, GPIO.IN)
    print("IR Sensor Ready.....")
    print(" ")
    GPIO.add_event_detect(sensor, GPIO.FALLING, 
            callback=ir_detection_callback, bouncetime=100)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()