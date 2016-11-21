from getch import getch
import time
from keybindings import keybindings
from recipes import recipes
from switch import switch

while True:
    button = getch()
    print("Input:", button)
    keynum = keybindings.key(button)
    print(keynum)
    if button == "/":
        for x in range(0, 9):
            switch.ledswitch(x, "r")
            try:
                menge = int(input("Menge eingeben"))
                switch.pump(x, menge)
                switch.ledswitch(x, "b")
            except ValueError:
                print("input is not an integer")
                switch.errorlight()
    
    if button == "@":
        button = "x"
        while button != "@":
            try:
                button = getch()
                switch.pumpswitch(int(button), 0.5)
            except:
                switch.errorlight()
            
    else:
        if keynum == -1:
            print("key not recognized")
            switch.errorlight()
        else:
            name = keybindings.cocktail(keynum)
            while recipes.execute(name) != "finished":
                time.sleep(3)
            print("Request finished without errors")
