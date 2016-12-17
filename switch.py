
import time
import RPi.GPIO as GPIO
from constants import constants

GPIO.setwarnings(False) #Schaltet Text-Output von GPIO.py aus
GPIO.setmode(GPIO.BOARD) #Steuerung verwendet nun BOARD-Nummern

#Pins werden für ihre Funktion konfiguriert
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

pump_index = [13, 12, 11, 10, 3, 7, 5, 8, 15, 16] #Die BOARD-Adressen der Pumpen 0-9 Slot 5 und 8 getauscht weil kaputt
led_index = [18, 19, 21, 22, 23, 24, 26, 29, 31, 32] #Die BOARD-Adressen der LED-Paare 0-9

class switch:

    def pumpswitch(self, ptime): #self= Pumpennummer ptime= zu pumpende Zeit
        address = pump_index.pop(self) #Adresse der Pumpe aus pump_index
        pump_index.insert(self, address)
        switch.ledswitch(self, "r")
        GPIO.output(address, GPIO.HIGH) #Pumpe einschalten
        time.sleep(ptime) #Zeit abwarten
        GPIO.output(address, GPIO.LOW) #Pumpe ausschalten
        switch.ledswitch(self, "b")

    def pump(self, cl): #self = Pumpennummer cl=Menge in cl
        if cl != 0:
            ptime = cl * constants.multiplier() + constants.distance(self) #Menge * Multiplikator um cl in Sekunden umzurechnen + Zeit bis Föüssigkeit das Ende des Schlauchs erreicht
            switch.pumpswitch(self, ptime)

    def ledswitch(self, color): #self = Nummer des LED-Paares color = r[ot] oder b[lau]
        address = led_index.pop(self) #Adresse des LED-Paares aus led_index
        led_index.insert(self, address)
        if color == "b":
            GPIO.output(address, GPIO.LOW) #Pin auf LOW Relais schaltet auf blau (Normalzustand)
        if color == "r":
            GPIO.output(address, GPIO.HIGH) #Pin auf HIGH Relais schaltet auf rot

    def errorlight(): #vorprogrammiertes rotes Lauflicht
        for x in range(10):
            switch.ledswitch(x, "r")
            time.sleep(0.1)
            switch.ledswitch(x, "b")
        



