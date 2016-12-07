import time
from switch import switch
from constants import constants

class recipes:

    def execute(self): #führt einprogrammierte Rezepte aus
        for x in range(10):
            element = self.pop(x) #Menge für erste Pumpe
            self.insert(x, element)           
            switch.pump(x, element) #Pumpe x einschalten Menge Element pumpen

    def cocktail(self):
        recipe = cocktails.pop(self) #Name des Cocktails bei gegebenen Index
        cocktails.insert(self, recipe)
        return recipe

cocktails = [screwdriver, orangefizz, pinapplefizz, bitterrussian, pinacolada, maitai, tomcollins, wodkafizz, springparadise, coolrussian, daiquiri, russischerspringer, sweetspring, stechmuecke, gintonic]
#Enthält alle eingespeicherten Rezepte in ihrer Reihenfolge auf der Tastatur

##################################################	Internet-Cocktails	################################################## Formatierung dieses Abschnitts abhängig vom Editor
screwdriver 		= [0, 0, 4, 0, 0, 0, 0, 0, 11, 0] #Angabe der Menge in cl für Pumpen 0-9
schlumpf 		= [0, 0, 4, 0, 0, 2, 0, 0, 0, 4]
orangefizz 		= [0, 5, 0, 0, 1, 0, 2, 0, 5, 0] #2cl Soda
coolrussian 		= [0, 0, 5, 5, 2, 0, 3, 0, 0, 0] 
wodkafizz		= [0, 0, 5, 0, 2, 0, 3, 0, 0, 0] #5cl Soda
russischerspringer	= [0, 0, 6, 0, 1, 3, 5, 0, 0, 0] 
bitterrussian 		= [1, 0, 4, 10, 0, 0, 0, 0, 0, 0]
daiquiri		= [5, 0, 0, 0, 1, 0, 0.5, 0, 0, 0]
maitai			= [5, 0, 0, 0, 0, 2, 2, 3, 3, 0]
pinapplefizz		= [5, 0, 0, 0, 1, 0, 3, 6, 0, 0]
pinacolada		= [5, 0, 0, 0, 0, 0, 0, 5, 0, 0] #5cl Cocos
tomcollins		= [0, 5, 0, 0, 2, 0, 3, 0, 0, 0] #5cl Soda
gintonic                = [0, 4, 0, 11, 0, 0, 0, 0, 0, 0,]             
##################################################	 Eigen-Cocktails	##################################################
leberzirrhose 		= [3, 3, 3, 6, 0, 0, 0, 0, 0, 0]
spassimglas 		= [0, 0, 4, 10, 0, 0, 0, 0, 0, 1]
hotlinemiami 		= [3, 2, 0, 0, 0, 0, 5, 5, 0, 0]
swimmingpool 		= [2, 0, 2, 0, 0, 1, 0, 6, 0, 2] #2cl Cocos
manapotion		= [2, 2, 2, 0, 0, 2, 3, 0, 0, 4]
thecockslapper		= [0, 4, 4, 0, 0, 0, 0, 2, 0, 4]
##################################################	Alkoholfreie-Cocktails	##################################################
springparadise		= [0, 0, 0, 0, 2, 0, 2, 3, 8, 0]
sweetspring		= [0, 0, 0, 0, 1, 1, 1, 9, 3, 0]
stechmuecke		= [0, 0, 0, 10, 1, 0, 3, 1, 0, 0]
virgincolada            = [0, 0, 0, 0, 0, 0, 0, 5, 7, 3]







