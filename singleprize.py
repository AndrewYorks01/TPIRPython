from prize import *
from random import randrange
import random

# Double Prices
def play_doubleprices():
    items = [] # generate the item database
    file = dir_path + larg_path # generate the filepath to the item bank
    print("\nDOUBLE PRICES")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        items.append(Large(*line.split()))

    size = len(items) # get the size of the item bank
    prize_id = randrange(size)
    prize = Large(items[prize_id].description, items[prize_id].shortname, items[prize_id].price)

    # generate the two prices
    correct_price = int(prize.price)
    wrong_price = correct_price
    while ( (abs(wrong_price - correct_price) <= 100 ) ):
        wrong_price = random.randint(5000, 9999)

    # if position is 0, the correct price is on top; if 1, the correct price is on the bottom
    position = randrange(2)

    print(prize.showPrize()) # show the prize
    if (position == 0):
        print("1. " + prize.showARP()) # correct price (the showARP() function already shows a dollar sign)
        print("2. $" + str(wrong_price)) # wrong price
    else:
        print("1. $" + str(wrong_price)) # wrong price
        print("2. " + prize.showARP()) # correct price (the showARP() function already shows a dollar sign)

    choosing = True
    while choosing:
        player_choice = input("What is the correct price?: ")
        try:
            player_choice = int(player_choice)
        except ValueError:
            continue
        if ( (player_choice == 1) or (player_choice == 2) ):
            choosing = False

    print("The actual retail price is " + prize.showARP())

    if (player_choice == position+1):
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose.")

    endgame()