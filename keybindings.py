keys = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "y", "x", "c", "v", "b", "n", "m", ",", "."]

class keybindings:
   
    def key(self):
        if keys.count(self) != 0:
            keyindex = keys.index(self)
            print("Keyindex is:", keyindex)
            return keyindex
        else:
            return -1
            

       


