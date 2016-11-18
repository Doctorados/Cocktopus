keys = ["q", ]
cocktails = ["screwdriver"]


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
       


