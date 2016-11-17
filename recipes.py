import time
from switch import switch
from constants import constants

class recipes:

    def execute(self):
        if self == "screwdriver":
            switch.pump(2, 5)
            time.sleep(constants.pause())
            switch.pump(8, 10)
            time.sleep(constants.pause())
            return "finished"



