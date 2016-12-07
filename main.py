from getch import getch
import time
from keybindings import keybindings
from recipes import recipes
from switch import switch

while True:
    button = getch()
    print("Input:", button)
    keyindex = keybindings.key(button)
    print(keyindex)
    if button == "/":
        for x in range(0, 9):
            switch.ledswitch(x, "r")
            try:
                cl = int(input("Menge eingeben"))
                switch.pump(x, cl)
                switch.ledswitch(x, "b")
            except ValueError:
                print("input is not an integer")
                switch.errorlight()

    if keyindex == -1:
        print("key not recognized")
        switch.errorlight()
    else:
        recipes.execute(recipes.cocktail(keyindex))
        print("Request finished without errors")
