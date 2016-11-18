class constants:

    def multiplier():
        return 0.25

    def distance(self):
        distancelist = [1, 0.5, 0.25, 0.125, 0, 0, 0.125, 0.25, 0.5, 1]
        value = distancelist.pop(self)
        distancelist.insert(self, value)
        return value
        


    def pause():
        return 1
