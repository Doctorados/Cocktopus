from getch import getch
from keybindings import keybindings
from recipes import recipes
from switch import switch

while True:
    button = getch() #Input (nur einzelnes Zeichen) ohne Notwendigkeit die Enter-Taste zu drücken
    keyindex = keybindings.key(button) #Eingabe wird der Eingabe eine Zahl zugewiesen
    if button == "/": #Manueller Modus
        for x in range(10):
            switch.ledswitch(x, "r") #Momentan ausgewählte Flasche leuchtet rot
            try:
                cl = int(input("Menge eingeben")) #Menge in cl eingeben mit Enter bestätigen
                switch.pump(x, cl) #Menge wir gepumpt
                switch.ledswitch(x, "b") #Beleuchtung zurück zu blau
            except ValueError:
                switch.errorlight() #rotes Lauflicht bei fehlerhafter Eingabe

    if keyindex == -1: #-1 = Fehler. True/False nicht möglich da in Python False=0 was gültiger Index ist
        switch.errorlight()#rotes Lauflicht bei fehlerhafter Eingabe
    else:
        recindex = recipes.cocktail(keyindex) #Index des Cocktailrezeptes in der Liste cocktails (recipes.py)
        recipes.execute(recindex) #Aufrufen der Funktion zur Ausführung des Rezepts.

