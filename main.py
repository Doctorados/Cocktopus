from getch import getch
import time
from keybindings import keybindings
from recipes import recipes
from switch import switch

while True:
    input = getch()
    print("Input:", input)
    keynum = keybindings.key(input)
    if keynum == "/":
        for x in range(1, 10):
        switch.ledswitch(x, "r")
        try:
            menge = int(input())
            switch.pump(x, menge)
            switch.ledswitch(x, "b")
        except ValueError:
            print("input is not an integer")
            switch.errorlight()

    else:
        if keynum != False:
            name = keybindings.cocktail(keynum)
            while recipes.execute(name) != "finished":
                time.sleep(3)
            print("Request finished without errors")
        else:
            print("key not recognized")
            switch.errorlight()
