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
    items = []
    first = Grocery("V8 Juice", "JUICE", 3.15)
    second = Grocery("Hot Pockets", "PIZZA SNACK", 2.49)
    third = Grocery("Alberto V05", "SHAMPOO", 3.49)
    items.append(first)
    items.append(second)
    items.append(third)
    random.shuffle(items)
    for i, item in enumerate(items):
        print(str(i+1) + ". " + item.showPrize())

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
                        
# Hi-Lo
def play_hilo():
    ggItems = [] # generate the item database
    file = dir_path + groc_path # generate the filepath to the item bank
    print("\nHI-LO")
    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        ggItems.append(Grocery(*line.split()))
    
    size = len(ggItems) # get the size of the item bank
    ids = random.sample(range(0, size+1), 6) # pick six different item IDs
    items = [] # generate the items
    picked = [False, False, False, False, False, False] # bools that check if each item has been chosen
    hiPrices = [0.00, 0.00, 0.00] # prices on the high row

    # set all the grocery items
    for number in range (0, 6):
       item = Grocery(ggItems[ids[number]].description, ggItems[ids[number]].shortname, ggItems[ids[number]].price)
       items.append(item)

    # show all the grocery items   
    for i, item in enumerate(items):
        print(str(i+1) + ". " + item.showPrize())

    picks = 0 # Items chosen

    while (picks < 3):
        # pick one of the prizes, ensuring that the player inputs a number
        selecting = True
        while selecting:
            player_choice = input("Which item (enter the number) do you want to pick?: ")
            try:
                player_choice = int(player_choice)
            except ValueError:
                print("\nPlease enter a digit.")
                continue
            if 1 <= player_choice <= 6:
                selecting = False
            else:
                print("\nPlease enter a number between 1 and 6.")

        # selecting an item
        if (picked[player_choice - 1]):
            print("\nYou've already purchased this item. Please pick another.")
        else:
            print("\nThe actual retail price of the " + items[player_choice-1].showShortName() + " is " + items[player_choice-1].showARP())
            print() # blank line
            picked[player_choice-1] = True # this item has been selected
            hiPrices[picks] = float(items[player_choice-1].price) # add the item's price to the hiPrices list

            # show all the grocery items
            for i, item in enumerate(items):
                if (picked[i] == True):
                    print(str(i+1) + ". " + item.showPrize() + " - " + item.showARP())
                else:
                    print(str(i+1) + ". " + item.showPrize())

            picks += 1 # add one pick

    # get the cheapest item on the HI shelf
    cheapest = min(hiPrices)
    print("\nThe cheapest price on the HI shelf is " + str(f"${cheapest:.2f}"))
    input("Now, let's reveal the prices of the remaining items... ")

    on = 0 # used in the reveal
    lost = False # checks if the player has lost

    # reveal the remaining prices
    print() # skip a line
    for number in range (0, 6):
        if ( (not picked[number]) and (not lost) ):
            on += 1
            if (float(items[number].price) > cheapest): # break out of the loop and show the lose message
                print("The actual retail price of the " + items[number].showShortName() + " is " + items[number].showARP())
                lost = True
            else:
                if (on < 3): # pause for input unless the player is on the last item
                    input("The actual retail price of the " + items[number].showShortName() + " is " + items[number].showARP())
                else:
                    print("The actual retail price of the " + items[number].showShortName() + " is " + items[number].showARP())
    
    if (lost == True):
        print("\nSorry, you lose.")
    else:
        print("\nCongratulations, you win!")
    endgame()

# Pick-a-Pair
def play_pickapair():
    ggItems = [] # generate the item database
    file = dir_path + groc_path # generate the filepath to the item bank
    print("\nPICK-A-PAIR")
    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        ggItems.append(Grocery(*line.split()))
    
    size = len(ggItems) # get the size of the item bank
    items = [] # generate the items
    picked = [False, False, False, False, False, False] # bools that check if each item has been chosen

    # Bools that check if each pair has been found.
    found_pair1 = False
    found_pair2 = False
    found_pair3 = False

    #print(ggItems[0].showPrize())

    # Check for pair 1.
    while (not found_pair1):
        first = randrange(size) # set the ID for item #1
        second = first # set the ID for item #2, matching #1 as a placeholder
        while (second == first): # change the ID to a different number
            second = randrange(size)

        # Load the IDs into the items themselves
        temp1 = Grocery(ggItems[first].description, ggItems[first].shortname, ggItems[first].price)
        temp2 = Grocery(ggItems[second].description, ggItems[second].shortname, ggItems[second].price)
        if (temp1.price == temp2.price):
            found_pair1 = True
            items.append(temp1)
            items.append(temp2)

    # Check for pair 2.
    while (not found_pair2):
        third = randrange(size) # set the ID for item #3
        fourth = third # set the ID for item #4, matching #1 as a placeholder
        while (fourth == third): # change the ID to a different number
            fourth = randrange(size)

        # Load the IDs into the items themselves
        temp3 = Grocery(ggItems[third].description, ggItems[third].shortname, ggItems[third].price)
        temp4 = Grocery(ggItems[fourth].description, ggItems[fourth].shortname, ggItems[fourth].price)
        if ( (temp3.price == temp4.price) and (temp3.price != temp1.price) ):
            found_pair2 = True
            items.append(temp3)
            items.append(temp4)

    # Check for pair 3.
    while (not found_pair3):
        fifth = randrange(size) # set the ID for item #5
        sixth = fifth # set the ID for item #6, matching #5 as a placeholder
        while (sixth == fifth): # change the ID to a different number
            sixth = randrange(size)

        # Load the IDs into the items themselves
        temp5 = Grocery(ggItems[fifth].description, ggItems[fifth].shortname, ggItems[fifth].price)
        temp6 = Grocery(ggItems[sixth].description, ggItems[sixth].shortname, ggItems[sixth].price)
        if ( (temp5.price == temp6.price) and (temp5.price != temp1.price) and (temp5.price != temp3.price) ):
            found_pair3 = True
            items.append(temp5)
            items.append(temp6)
    
    random.shuffle(items) # shuffle the items

    # show all the grocery items   
    for i, item in enumerate(items):
        print(str(i+1) + ". " + item.showPrize())

    # pick one of the prizes, ensuring that the player inputs a number
    selecting = True
    while selecting:
        choice1 = input("Which item (enter the number) do you want to pick?: ")
        try:
            choice1 = int(choice1)
        except ValueError:
            print("\nPlease enter a digit.")
            continue
        if 1 <= choice1 <= 6:
            selecting = False
        else:
            print("\nPlease enter a number between 1 and 6.")

    print("\nThe actual retail price of the " + items[choice1-1].showShortName() + " is " + items[choice1-1].showARP())

    # ask the player to pick an item that has the same price as the first item
    selecting2 = True
    while selecting2:
        choice2 = input("Now, which item do you think has the same price?: ")
        try:
            choice2 = int(choice2)
        except ValueError:
            print("\nPlease enter a digit.")
            continue
        if (choice2 == choice1):
            print("\nYou can't pick the same item.")
        elif 1 <= choice2 <= 6:
            selecting2 = False
        else:
           print("\nPlease enter a number between 1 and 6.")

    print("\nThe actual retail price of the " + items[choice2-1].showShortName() + " is " + items[choice2-1].showARP())

    if (float(items[choice1-1].price) == float(items[choice2-1].price)):
        print("Congratulations, you win!")
    else:
        # second chance
        print("That's not correct, but you get a second chance.")
        print()
        print("1. " + items[choice1-1].showPrize())
        print("2. " + items[choice2-1].showPrize())

        # choosing item to keep
        selecting3 = True
        while selecting3:
            to_keep = input("Which item do you want to keep?: ")
            try:
                to_keep = int(to_keep)
            except ValueError:
                print("\nPlease enter a number between 1 and 2.")
            if 1 <= to_keep <= 2:
                selecting3 = False
        if (to_keep == 1):
            temp_price = float(items[choice1-1].price)
        else:
            temp_price = float(items[choice2-1].price)

        # one more chance
        selecting4 = True
        while selecting4:
            choice3 = input("Now, which item do you think is " + str(f"${temp_price:.2f}?: "))
            try:
                choice3 = int(choice3)
            except ValueError:
                print("\nPlease enter a digit.")
            if ( (choice3 == choice1) or (choice3 == choice2) ):
                print("\nYou can't pick an item you've already picked.")
            elif 1 <= choice3 <= 6:
                selecting4 = False
            else:
                print("\nPlease enter a number between 1 and 6.")
        
        # reveal the item's price
        print("\nThe actual retail price of the " + items[choice3-1].showShortName() + " is " + items[choice3-1].showARP())

        if (float(items[choice3-1].price) == temp_price):
            print("Congratulations, you win!")
        else:
            print("Sorry, you lose.")

    endgame()

    
        

        
        









    