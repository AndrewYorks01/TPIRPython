from prize import *
from random import randrange
import random

# Generate a wrong price in higher/lower games like Bonus Game.
def generate_hl_price(price, higher_or_lower):
    p = int(price)
    val = int(higher_or_lower)
    result = p
    if (val == 0): # generate a fake price that's too low (HIGHER)
        if (p < 50):
            while (abs(p-result) < 5):
                result = random.randint(8, p)
        else:
            while (abs(p-result) < 5):
                result = random.randint(50, p)           
    else:
        while (abs(p-result) < 5):
            result = random.randint(p, p+20)
    return result

# Bonus Game
def play_bonusgame():
    all_items = [] # generate the item database
    file = dir_path + smal_path # generate the filepath to the item bank
    print("\nBONUS GAME") 

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        all_items.append(Small(*line.split()))

    size = len(all_items) # get the size of the item bank
    ids = random.sample(range(0, size+1), 4) # pick five different item IDs
    items = [] # generate the items
    controlled = [False, False, False, False] # spaces the player has controlled
    bonus_window = randrange(4) # window with the bonus
    wrongPrices = [0, 0, 0, 0] # wrong prices

    # if these are set to 0, the wrong price will be too low (guess HIGHER)
    # if these are set to 1, the wrong price will be too high (guess LOWER)
    wrongValues = [2, 2, 2, 2] # initialization
    for v in range (0, 4):
        wrongValues[v] = randrange(2)

    # set all the items
    for number in range (0, 4):
       item = Small(all_items[ids[number]].description, all_items[ids[number]].shortname, all_items[ids[number]].price)
       items.append(item)

    # set the wrong prices
    for pr in range (0, 4):
        wrongPrices[pr] = generate_hl_price(int(items[pr].price), int(wrongValues[pr]))

    # start gameplay
    for on in range(0, 4):
        print(str(on+1) + ". " + items[int(on)].showPrize()) # display the item
        print("$" + str(wrongPrices[int(on)])) # display the wrong price
        guessing = True # loop until the player inputs an H or an L in either case
        while (guessing):
            player_choice = input("This price is wrong. \nIs the correct price higher (H) or lower (L)?: ")
            if ((player_choice == "H") or (player_choice == "h") or (player_choice == "L") or (player_choice == "l") ):
                guessing = False # exit loop
            else:
                pass # go through loop again
        print("The actual retail price is " + items[on].showARP())

        # correct guess of HIGHER
        if ( ((player_choice == "H") or (player_choice == "h")) and ( int(items[on].price) >= int(wrongPrices[int(on)]) ) ):
            print("That's correct! You've earned control of this space.")
            controlled[int(on)] = True

        # correct guess of LOWER
        elif ( ((player_choice == "L") or (player_choice == "l")) and ( int(items[on].price) <= int(wrongPrices[int(on)]) ) ):
            print("That's correct! You've earned control of this space.")
            controlled[int(on)] = True

        else:
            print("Sorry, that's not correct.")
        print() # line break

    # results
    print("The bonus is behind window #" + str(bonus_window + 1) )
    if (controlled[int(bonus_window)] == True):
        print("Congratulations, you win!")
    elif ( (not controlled[0]) and (not controlled[1]) and (not controlled[2]) and (not controlled[3]) ): 
        print("Well... you're not the biggest loser, but you're in the top five.")
    else:
        print("Sorry, you lose.")

    endgame()