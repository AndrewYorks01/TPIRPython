from prize import *
import os
import pathlib
from random import randrange
import random

def compatible_for_bullseye(price):
    p = float(price)
    if (p > 12):
        return False
    elif ((p > 4) and (p < 5)):
        return False
    elif ((p > 6) and (p < 10)):
        return False
    elif ((p > 3) and (p < 3.34)):
        return False
    elif ((p > 2.40) and (p < 2.50)):
        return False
    else:
        return True
    

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

# Bullseye
def play_bullseye():
    ggItems = [] # generate the item database
    file = dir_path + groc_path # generate the filepath to the item bank
    print("\nBULLSEYE") 

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        if (compatible_for_bullseye(Grocery(*line.split()).price)): # only extract items with Bullseye-compatible prices
            ggItems.append(Grocery(*line.split()))

    size = len(ggItems) # get the size of the item bank
    ids = random.sample(range(0, size+1), 5) # pick five different item IDs
    items = [] # generate the items
    picked = [False, False, False, False, False] # bools that check if each item has been purchased
    has_marking = [False, False, False, False, False] # determines if a chosen prize is on the board (between $2-$10)
    picks = 0 # how many products the player has chosen
    won = False
    hidden_bullseye = randrange(5) # location of the hidden bullseye

    # set all the grocery items
    for number in range (0, 5):
       item = Grocery(ggItems[ids[number]].description, ggItems[ids[number]].shortname, ggItems[ids[number]].price)
       items.append(item)

    # show all the grocery items   
    for i, item in enumerate(items):
        print(str(i+1) + ". " + item.showPrize())

    while ((picks < 3) and (not won)):
        print("Picks remaining: " + str(3-picks))

        # pick one of the prizes, ensuring that the player inputs a number
        selecting = True
        while (selecting):
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

        # buying an item
        if (picked[player_choice - 1]):
            print("\nYou've already picked this item. Please pick another.")
        else:
            print("\nYou picked the " + items[player_choice-1].showShortName())
            buying = True
            # input how many of the item the player wants to buy, ensuring the player inputs a nonzero integer
            while buying:
                tobuy = input("How many do you want?: ")
                try:
                    tobuy = int(tobuy)
                except ValueError:
                    print("\nPlease enter a valid number.")
                    continue
                if tobuy > 0:
                    buying = False
                else:
                    print("\nYou can't pick zero of something.")

            # calculate the total
            print("\nEach one is " + items[player_choice-1].showARP())
            total = float(items[player_choice-1].price) * tobuy
            print("For a total of " + str(f"${total:.2f}"))
            if (total >= 10 and total <= 12): # on the bullseye
                won = True
            elif (total >= 2 and total < 10): # on the target, but not the bullseye
                print("\nYou didn't hit the bullseye, but you do get a mark for this item.")
                picked[player_choice-1] = True # the player has chosen this item
                has_marking[player_choice-1] = True # this item has a mark
                picks += 1
            else: # not on the target at all
                print("\nYou completely missed the target. You don't get a mark for this item.")
                picked[player_choice-1] = True # the player has chosen this item
                picks += 1
        
        # display the groceries again
        if ( (not won) and (picks < 3) ):
            print()
            for i, item in enumerate(items):
                if ( (picked[i] == True) and (has_marking[i] == True) ):
                    print(str(i+1) + ". " + item.showPrize() + " - O")
                elif ( (picked[i] == True) and (has_marking[i] == False) ):
                    print(str(i+1) + ". " + item.showPrize() + " - X")
                else:
                    print(str(i+1) + ". " + item.showPrize())

    # win conditions
    if (won):
        print("\nCongratulations, you win!")
    elif ( (has_marking[0] == False) and (has_marking[1] == False) and (has_marking[2] == False) and (has_marking[3] == False) and (has_marking[4] == False) ):
        print("\nSorry, you lose.")
    else:
        print("\nYou didn't hit the bullseye, but let's see if you found the hidden bullseye.")

        # Find the hidden bullseye
        for find in range (0, 5):
            if (has_marking[find] and (not won)): # only reveal items on the board
                input("Let's look behind the " + items[find].showShortName() + ": ")
                if (find == hidden_bullseye):
                    won = True
                else:
                    print("Sorry, it's not behind this item.")
    
        if (won):
            print("Congratulations, you win!")
        else:
            print("\nSorry, you lose.")

    endgame()

# Check-Out
def play_checkout():
    ggItems = [] # generate the item database
    file = dir_path + groc_path # generate the filepath to the item bank
    print("\nCHECK-OUT")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        ggItems.append(Grocery(*line.split()))
    
    size = len(ggItems) # get the size of the item bank
    ids = random.sample(range(0, size+1), 5) # pick five different item IDs
    items = [] # generate the items

    # set all the grocery items
    for number in range (0, 5):
       item = Grocery(ggItems[ids[number]].description, ggItems[ids[number]].shortname, ggItems[ids[number]].price)
       items.append(item)

    prices = [0.0, 0.0, 0.0, 0.0, 0.0] # prices the player inputs
    player_total = 0.0 # total of player's prices
    actual_total = 0.0 # total of the actual retail prices

    # where the player inputs all the prices
    for x in range (0, 5):
        print(str(x+1) + ". " + items[x].showPrize())
        inputting = True
        while inputting:
            prices[x] = input("$")
            try:
                prices[x] = float(prices[x])
            except ValueError:
                print("Please enter a price.")
                continue
            if (prices[x] >= 0.01):
                inputting = False
                player_total = player_total + prices[x]
    
    print("Your total: " + str(f"${player_total:.2f}"))
    input("Now, let's reveal the actual prices of the items... ")
    print()

    # reveal each item's actual retail price
    for y in range (0, 5):
        actual_total = actual_total + float(items[y].price)
        input("The actual retail price of the " + items[y].showShortName() + " is " + items[y].showARP())
    
    # reveal the total and difference
    print("\nThe total of the ARPs is " + str(f"${actual_total:.2f}"))
    difference = abs(float(player_total) - float(actual_total))
    print("For a difference of " + str(f"${difference:.2f}"))

    if (difference <= 2):
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose.")

    endgame()

# Grocery Game
def play_grocerygame():
    ggItems = [] # generate the item database
    file = dir_path + groc_path # generate the filepath to the item bank
    print("\nGROCERY GAME")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        ggItems.append(Grocery(*line.split()))
    
    size = len(ggItems) # get the size of the item bank
    ids = random.sample(range(0, size+1), 5) # pick five different item IDs
    items = [] # generate the items
    picked = [False, False, False, False, False] # bools that check if each item has been purchased
    boughtFive = False # bools that check if all five items have been purchased

    # set all the grocery items
    for number in range (0, 5):
       item = Grocery(ggItems[ids[number]].description, ggItems[ids[number]].shortname, ggItems[ids[number]].price)
       items.append(item)

    running_total = 0.0 # the player's running total
    won = False # checks if the player has won

    # show all the grocery items   
    for i, item in enumerate(items):
        print(str(i+1) + ". " + item.showPrize())

    # continue gameplay until the player wins or loses
    while ((running_total <= 22) and (boughtFive == False) and (won == False)):
        print("Running total: " + str(f"${running_total:.2f}"))

        # pick one of the prizes, ensuring that the player inputs a number
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

        # buying an item
        if (picked[player_choice - 1]):
            print("\nYou've already purchased this item. Please pick another.")
        else:
            print("\nYou picked the " + items[player_choice-1].showShortName())
            buying = True
            # input how many of the item the player wants to buy, ensuring the player inputs a nonzero integer
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
            
            # add to the total
            print("\nEach one is " + items[player_choice-1].showARP())
            total = float(items[player_choice-1].price) * tobuy
            print("For a total of " + str(f"${total:.2f}"))
            print()
            running_total = running_total + total

            picked[player_choice-1] = True # the item has been selected

            # check if the player has won or lost
            if ( (picked[0] == True) and (picked[1] == True) and (picked[2] == True) and (picked[3] == True) and (picked[4] == True) ):
                boughtFive = True
            if ( (running_total >= 20) and (running_total <= 22) ):
                won = True

            # display the groceries again
            if ( (not won) and (running_total <= 22) ):
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

    endgame()
                        
    







    