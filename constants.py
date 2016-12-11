class constants:

    def multiplier(): #cl*multiplier = Zeit in Sekunden in der ein cl gepumpt wird
        return 0.25

    def distance(self): #self = Pumpennummer
        distancelist = [0, 0, 0, 0, 0, 0, 0, 0, 0, ] #War doch nicht nötig
        value = distancelist.pop(self)
        distancelist.insert(self, value)
        return value
