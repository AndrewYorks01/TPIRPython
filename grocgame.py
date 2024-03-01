from prize import *
import os
import pathlib
from random import randrange
import random

def test():
    print("TEST")
    while True:
        value = input("Enter a number between 0 and 100:")
        try:
            value = int(value)
        except ValueError:
            print("Valid number, please")
            continue
        if 0 <= value <= 100:
            break
        else:
            print("Please enter a number between 1 and 100")

# Grocery Game
def play_grocerygame():
    ggItems = []
    drc = pathlib.Path(__file__).parent.resolve() # get directory
    file = str(drc) + "\prizes\grocery.txt"
    print()
    print("GROCERY GAME")
    lines = open(file).readlines()
    for line in lines:
        ggItems.append(Grocery(*line.split()))
    #for gg in ggItems:
    #    print(gg.showPrize() + ", " + gg.showShortName() + ", " + gg.showARP())
    size = len(ggItems)
    #print("Items: " + str(size))
    #print(randrange(size))
    ids = random.sample(range(0, size+1), 5)
    items = []
    picked = [False, False, False, False, False]
    boughtFive = False
    iter = 0

    for number in range (0, 5):
       item = Grocery(ggItems[ids[number]].description, ggItems[ids[number]].shortname, ggItems[ids[number]].price)
       items.append(item)

    running_total = 0.0
    won = False
       
    for i, item in enumerate(items):
        print(str(i+1) + ". " + item.showPrize())

    while ((running_total <= 22) and (boughtFive == False) and (won == False)):
        print("Running total: " + str(f"${running_total:.2f}"))
        selecting = True
        while selecting:
            player_choice = input("Which item (enter the number) would you like to buy?: ")
            try:
                player_choice = int(player_choice)
            except ValueError:
                print("\nPlease enter a digit.")
                continue
            if 1 <= player_choice <= 5:
                selecting = False
            else:
                print("\nPlease enter a number between 1 and 5.")

        #print(player_choice)

        if (picked[player_choice - 1]):
            print("\nYou've already purchased this item. Please pick another.")
        else:
            print("\nYou picked the " + items[player_choice-1].showShortName())
            buying = True
            while buying:
                tobuy = input("How many do you want to buy?: ")
                try:
                    tobuy = int(tobuy)
                except ValueError:
                    print("\nPlease enter a valid number.")
                    continue
                if tobuy > 0:
                    buying = False
                else:
                    print("\nYou can't buy zero of something.")
            print("\nEach one is " + items[player_choice-1].showARP())
            total = float(items[player_choice-1].price) * tobuy
            #print(total)
            print("For a total of " + str(f"${total:.2f}"))
            print()
            running_total = running_total + total
            picked[player_choice-1] = True
            if ( (picked[0] == True) and (picked[1] == True) and (picked[2] == True) and (picked[3] == True) and (picked[4] == True) ):
                boughtFive = True
            if ( (running_total >= 20) and (running_total <= 22) ):
                won = True
            if (not won):
                for i, item in enumerate(items):
                    if (picked[i] == True):
                        print(str(i+1) + ". " + item.showPrize() + " - " + item.showARP())
                    else:
                        print(str(i+1) + ". " + item.showPrize())
        # End while loop

    print("Running total: " + str(f"${running_total:.2f}"))          
    if (won == True):
        print("\nCongratulations, you win!")
    elif ( (running_total < 20) or (running_total > 22) ):
        print("\nSorry, you lose.")
    else:
        print("\nCongratulations, you win!")
    input("Press any key to continue: ")
    os.system('cls')
                        
    







    