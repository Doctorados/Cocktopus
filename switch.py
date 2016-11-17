
import time
import RPi.GPIO as GPIO
from constants import constants

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Pumpe 1
GPIO.setup(2, GPIO.OUT)
#Pumpe 2
GPIO.setup(3, GPIO.OUT)
#Pumpe 3
GPIO.setup(4, GPIO.OUT)
#Pumnpe 4
GPIO.setup(17, GPIO.OUT)
#Pumpe 5
GPIO.setup(27, GPIO.OUT)
#Pumpe 6
GPIO.setup(22, GPIO.OUT)
#Pumpe 7
GPIO.setup(10, GPIO.OUT)
#Pumpe 8
GPIO.setup(9, GPIO.OUT)
#Pumpe 9
GPIO.setup(11, GPIO.OUT)
#Pumpe 10
GPIO.setup(0, GPIO.OUT)

#LED_Slot 1
GPIO.setup(5, GPIO.OUT)
#Led Slot 2
GPIO.setup(6, GPIO.OUT)
#Led Slot 3
GPIO.setup(13, GPIO.OUT)
#Led Slot 4
GPIO.setup(19, GPIO.OUT)
#Led Slot 5
GPIO.setup(26, GPIO.OUT)
#Led Slot 6
GPIO.setup(14, GPIO.OUT)
#Led Slot 7
GPIO.setup(15, GPIO.OUT)
#Led Slot 8
GPIO.setup(18, GPIO.OUT)
#Led Slot 9
GPIO.setup(23, GPIO.OUT)
#Led Slot 10
GPIO.setup(24, GPIO.OUT)

pump_index = [2, 3, 4, 17, 27, 22, 10, 9, 11, 0]
led_index = [5, 6, 13, 19, 26, 14, 15, 18, 23, 24]

class switch:

    def pumpswitch(self, zeit):
        port = pump_index.pop(self)
        pump_index.insert(self, port)
        GPIO.output(port, GPIO.HIGH)
        print(port, "set to high")
        time.sleep(zeit)
        GPIO.output(port, GPIO.LOW)
        print(port, "set to low")

    def pump(self, menge):
        zeit = (menge * constants.multiplier()) + constants.distance(self)
        switch.pumpswitch(self, zeit)

    def ledswitch(self, color):
        port = led_index.pop(self)
        led_index.insert(self, port)
        if color = "r":
            GPIO.output(port, GPIO.LOW)
            print(port, "set to low")
        if color = "b":
            GPIO.output(port, GPIO.HIGH)
            print(port, "set to high")

    def errorlight(self):
        for x in range(1, 10):
            ledswitch(x, "r")
            time.sleep(0.1)
            ledswitch(x, "b")




