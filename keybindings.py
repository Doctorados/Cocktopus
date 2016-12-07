keys = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'"]
#"y", "x", "c", "v", "b", "n", "m", ",", "."]
#Enthält mit Rezepten belegte Tasten in ihrer Reihenfolge auf der Tastatur (von links nach rechts, von oben nach unten)

class keybindings:
   
    def key(self):
        if keys.count(self) != 0: #prüft ob Eingabe in Liste vorkommt
            keyindex = keys.index(self) #Index der Eingabe in der Liste
            return keyindex
        else:
            return -1 #Fehlercode
            

       


