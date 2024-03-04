from prize import *
from random import randrange
import random

# Most Expensive
def play_mostexpensive():
    
    all_items = [] # generate the item database
    file = dir_path + med_path # generate the filepath to the item bank
    print("\nMOST EXPENSIVE")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        if (int(Medium(*line.split()).price) >= 1000):
            all_items.append(Medium(*line.split()))

    size = len(all_items) # get the size of the item bank
    ids = random.sample(range(0, size+1), 3) # pick five different item IDs
    items = [] # generate the items

    # set all the items
    for number in range (0, 3):
       item = Medium(all_items[ids[number]].description, all_items[ids[number]].shortname, all_items[ids[number]].price)
       items.append(item)

    # show the items
    for p in range (0, 3):
        print(str(p+1) + ". " + items[p].showPrize())

    # ask the player to pick the most expensive item, ensuring proper input
    selecting = True
    while (selecting):
        player_choice = input("Which prize (enter the number) is the most expensive?: ")
        try:
            player_choice = int(player_choice)
        except ValueError:
            continue
        if 1 <= player_choice <= 3:
            selecting = False

    # assign variables denoting the two products the player didn't choose
    if (player_choice == 1):
        first = 1
        second = 2
    elif (player_choice == 2):
        first = 0
        second = 2
    else:
        first = 0
        second = 1

    # price reveals
    print() # line break
    input("The actual retail price of the " + items[first].showShortName() + " is " + items[first].showARP() + " ")
    input("The actual retail price of the " + items[second].showShortName() + " is " + items[second].showARP() + " ")
    print("The actual retail price of the " + items[player_choice - 1].showShortName() + " is " + items[player_choice - 1].showARP())
    if ( (items[player_choice - 1].price >= items[first].price) and (items[player_choice - 1].price >= items[second].price) ):
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose.")

    endgame()

# One Wrong Price
def play_onewrongprice():
    all_items = [] # generate the item database
    file = dir_path + med_path # generate the filepath to the item bank
    print("\nONE WRONG PRICE")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        if (int(Medium(*line.split()).price) >= 1000):
            all_items.append(Medium(*line.split()))

    size = len(all_items) # get the size of the item bank
    ids = random.sample(range(0, size+1), 3) # pick five different item IDs
    items = [] # generate the items

    # set all the items
    for number in range (0, 3):
       item = Medium(all_items[ids[number]].description, all_items[ids[number]].shortname, all_items[ids[number]].price)
       items.append(item)

    with_wrong = randrange(3) # determines the prize with the wrong price
    
    # set the wrong price
    wrong_price = int(items[with_wrong].price)
    while ( (abs(wrong_price - int(items[with_wrong].price)) <= 100 ) ):
        wrong_price = random.randint(1000, 4500)

    # show the items and the given prices
    for p in range (0, 3):
        if (p == with_wrong):
            print(str(p+1) + ". " + items[p].showPrize() + " - $" + str(wrong_price) )
        else:
            print(str(p+1) + ". " + items[p].showPrize() + " - " + items[p].showARP())

    # ask the player to pick the most expensive item, ensuring proper input
    selecting = True
    while (selecting):
        player_choice = input("Which item has the one wrong price?: ")
        try:
            player_choice = int(player_choice)
        except ValueError:
            continue
        if 1 <= player_choice <= 3:
            selecting = False

    # results
    print("The actual retail price of the " + items[player_choice-1].showShortName() + " is " + items[player_choice-1].showARP())
    if (player_choice-1 == with_wrong):
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose. \nThe correct answer was the " + items[with_wrong].showShortName() + ".")

    endgame()    