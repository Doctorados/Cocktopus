import time
from switch import switch
from constants import constants

class recipes:

    def execute(self):
        for x in range(10):
            switch.pump(x, self.pop(x))
            time.sleep(constants.pause())
        return "finished"

    def cocktail(self):
        recipe = cocktails.pop(self)
        cocktails.insert(self, recipe)
        print("Cocktail is:", recipe)
        return recipe

screwdriver = [0, 0, 4, 0, 0, 0, 0, 0, 10, 0]

cocktails = [screwdriver, orangefizz, pinapplefizz, bitterrussian, pinacolada, ipanema, maitai, tomcollins, wodkafizz, springparadise, coolrussian, daiquiri, russischerspringer]

