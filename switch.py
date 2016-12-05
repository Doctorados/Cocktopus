
import time
import RPi.GPIO as GPIO
from constants import constants

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Pumpe 1
GPIO.setup(13, GPIO.OUT)
#Pumpe 2
GPIO.setup(12, GPIO.OUT)
#Pumpe 3
GPIO.setup(11, GPIO.OUT)
#Pumnpe 4
GPIO.setup(10, GPIO.OUT)
#Pumpe 5
GPIO.setup(8, GPIO.OUT)
#Pumpe 6
GPIO.setup(7, GPIO.OUT)
#Pumpe 7
GPIO.setup(5, GPIO.OUT)
#Pumpe 8
GPIO.setup(3, GPIO.OUT)
#Pumpe 9
GPIO.setup(15, GPIO.OUT)
#Pumpe 10
GPIO.setup(16, GPIO.OUT)

#LED_Slot 1
GPIO.setup(18, GPIO.OUT)
#Led Slot 2
GPIO.setup(19, GPIO.OUT)
#Led Slot 3
GPIO.setup(21, GPIO.OUT)
#Led Slot 4
GPIO.setup(22, GPIO.OUT)
#Led Slot 5
GPIO.setup(23, GPIO.OUT)
#Led Slot 6
GPIO.setup(24, GPIO.OUT)
#Led Slot 7
GPIO.setup(26, GPIO.OUT)
#Led Slot 8
GPIO.setup(29, GPIO.OUT)
#Led Slot 9
GPIO.setup(31, GPIO.OUT)
#Led Slot 10
GPIO.setup(32, GPIO.OUT)

pump_index = [13, 12, 11, 10, 8, 7, 5, 3, 15, 16]
led_index = [18, 19, 21, 22, 23, 24, 26, 29, 31, 32]

class switch:

    def pumpswitch(self, ptime):
        address = pump_index.pop(self)
        pump_index.insert(self, address)
        GPIO.output(address, GPIO.HIGH)
        print(address, "set to high")
        time.sleep(ptime)
        GPIO.output(port, GPIO.LOW)
        print(address, "set to low")

    def pump(self, cl):
        if cl != 0:
            ptime = menge * constants.multiplier() + constants.distance(self)
            switch.pumpswitch(self, ptime)

    def manpump(self, bit):
        address = pump_index.pop(self)
        pump_index.insert(self, address)
        if bit == 1:
            GPIO.output(address, GPIO.HIGH)
            print(address, "set to high")
        else:
            GPIO.output(address, GPIO.LOW)
            print(address, "set to high")
        
        GPIO.output(address, GPIO.LOW)
        print(address, "set to low")

    def ledswitch(self, color):
        address = led_index.pop(self)
        led_index.insert(self, address)
        if color == "r":
            GPIO.output(address, GPIO.LOW)
            print(address, "set to low")
        if color == "b":
            GPIO.output(port, GPIO.HIGH)
            print(port, "set to high")

    def errorlight():
        for x in range(10):
            switch.ledswitch(x, "r")
            time.sleep(0.1)
            switch.ledswitch(x, "b")
        



