class constants:

    def multiplier(): #cl*multiplier = Zeit in Sekunden in der ein cl gepumpt wird
        return 0.25

    def distance(self): #self = Pumpennummer
        distancelist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #Für Pumpen 0-9 !!!Werte nur Platzhalter!!!
        value = distancelist.pop(self)
        distancelist.insert(self, value)
        return value
