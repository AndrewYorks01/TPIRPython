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
                result = random.randint(7, p)
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
    ids = random.sample(range(0, size), 4) # pick four different item IDs
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

# Cliff Hangers
def play_cliffhangers():
    all_items = [] # generate the item database
    file = dir_path + smal_path # generate the filepath to the item bank
    print("\nCLIFF HANGERS") 

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        all_items.append(Small(*line.split()))

    size = len(all_items) # get the size of the item bank
    items = [] # generate the items

    # Checks for each item
    found_item1 = False
    found_item2 = False
    found_item3 = False

    # find prizes that meet the criteria
    while (not found_item1): # item #1
        first = randrange(size)
        temp1 = Small(all_items[first].description, all_items[first].shortname, all_items[first].price)
        if (15 <= int(temp1.price) <= 25):
            found_item1 = True
            items.append(temp1)

    while (not found_item2): # item #2
        second = first # make sure to pick a different ID
        while (second == first):
            second = randrange(size)
        temp2 = Small(all_items[second].description, all_items[second].shortname, all_items[second].price)
        if (25 <= int(temp2.price) <= 35):
            found_item2 = True
            items.append(temp2)
        
    while (not found_item3): # item #3
        third = first # make sure to pick a different ID
        while ((third == first) or (third == second)):
            third = randrange(size)
        temp3 = Small(all_items[third].description, all_items[third].shortname, all_items[third].price)
        if (35 <= int(temp3.price) <= 45):
            found_item3 = True
            items.append(temp3)

    steps = 0 # Position of the mountain climber
    lost = False # check if the player has lost

    for on in range (0, 3):
        if (not lost):
            print("Position: " + str(steps))
            print(str(on+1) + ". " + items[on].showPrize())
            guessing = True
            while guessing:
                guess = input("What is the price?: $")
                try:
                    guess = int(guess)
                except ValueError:
                    continue
                else:
                    guessing = False
            print("The actual retail price is " + items[on].showARP())
            difference = abs(guess - int(items[on].price)) # difference between player's guess and ARP
            steps += difference
            if (difference == 0): # bid is exactly right
                print("You were exactly right!")
            if (difference != 0):
                print("You were off by $" + str(difference))
            if (steps > 25): # climber falls off the cliff
                lost = True
            print() # empty line

    if (lost):
        print("Sorry, you lose.")
    else:
        print("Position: " + str(steps))
        print("Congratulations, you win!")

    endgame()

# Shell Game
def play_shellgame():
    all_items = [] # generate the item database
    file = dir_path + smal_path # generate the filepath to the item bank
    print("\nSHELL GAME") 

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        all_items.append(Small(*line.split()))

    size = len(all_items) # get the size of the item bank
    ids = random.sample(range(0, size), 4) # pick four different item IDs
    items = [] # generate the items
    has_chip = [" ", " ", " ", " "] # shells with a chip next to them
    ball_shell = randrange(4) # shell with the ball under it
    wrongPrices = [0, 0, 0, 0] # wrong prices
    chips_earned = 0

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
        placing_chip = False
        print("O O O O")
        print(has_chip[0] + " " + has_chip[1] + " " + has_chip[2] + " " + has_chip[3])
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
            chips_earned += 1
            print("That's correct!")
            placing_chip = True

        # correct guess of LOWER
        elif ( ((player_choice == "L") or (player_choice == "l")) and ( int(items[on].price) <= int(wrongPrices[int(on)]) ) ):
            chips_earned += 1
            print("That's correct!")
            placing_chip = True

        else:
            print("Sorry, that's not correct.")

        if (placing_chip):
            placing_loop = True
            while (placing_loop):
                shell_choice = input("Which shell (1-4) do you want to place a chip next to?: ")
                try:
                    shell_choice = int(shell_choice)
                except ValueError:
                    continue
                if ( (shell_choice < 1) or (shell_choice > 4) ):
                    pass
                elif (has_chip[shell_choice-1] == "*"): # shell already has a ball under it
                    pass
                else:
                    has_chip[shell_choice-1] = "*"
                    placing_loop = False
        print() # line break

    # results
    print("O O O O")
    print(has_chip[0] + " " + has_chip[1] + " " + has_chip[2] + " " + has_chip[3])
    
    if (chips_earned == 0):
        print("Sorry, you lose.")
    elif (chips_earned == 4):
        bonus_loop = True
        while (bonus_loop):
            bonus_chip = input("You won all 4 chips, but for a cash bonus, \nwhich shell has the ball behind it?: ")
            try:
                bonus_chip = int(bonus_chip)
            except ValueError:
                continue
            if ( (shell_choice < 1) or (shell_choice > 4) ):
                pass
            else:
                bonus_loop = False
        print("The ball is under shell #" + str(ball_shell + 1))
        if ( int(bonus_chip-1) == int(ball_shell) ):
            print("Congratulations, you win the prize and a cash bonus!")
        else:
            print("You didn't win the cash bonus, but you did win the prize.")
    else:
        input("Let's see which shell the ball is behind... ")
        print("The ball is under shell #" + str(ball_shell + 1))
        if (has_chip[ball_shell] == "*"):
            print("Congratulations, you win!")
        else:
            print("Sorry, you lose.")

    endgame()