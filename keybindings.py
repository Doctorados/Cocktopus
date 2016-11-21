keys = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "y", "x", "c", "v", "b", "n", "m", ",", "."]
cocktails = ["screwdriver", "orangefizz", "pinapplefizz", "bitterrussian", "pinacolada", "ipanema", "maitai", "tomcollins", "wodkafizz", "springparadise", "coolrussian", "daiquiri", "russischerspringer",  ]


class keybindings:
   
    def key(self):
        if keys.count(self) != 0:
            keyindex = keys.index(self)
            print("Keyindex is:", keyindex)
            return keyindex
        else:
            return -1
            
    def cocktail(self):
        cocktailname = cocktails.pop(self)
        cocktails.insert(self, cocktailname)
        print("Cocktail is:", cocktailname)
        return cocktailname
       


