from prize import *
from random import randrange
import random

# Checks if a price works in Coming or Going
def compatible_for_cog(price):
    p = int(price)
    if (p % 10 == 0): # the price can't end in 0
        return False
    elif (p > 9999): # the price can't be more than 4 digits
        return False
    else:
        lst = [int(i) for i in str(p)] # put each digit into a list
        if ( (lst[3] == 1) or (lst[3] == 2) ): # the price can't end in 1 or 2
            return False
        elif ( (lst[0] == lst[3]) and (lst[1] == lst[2]) ): # the price can't be a palindrome
            return False
        else:
            return True
        
# Checks if a price works in Flip Flop
def compatible_for_flipflop(price):
    p = int(price)
    if (p > 9999): # the price can't be mroe than 4 digits
        return False
    else:
        lst = [int(i) for i in str(p)] # put each digit into a list
        if (lst[0] == lst[1]): # first and second digits can't be the same
            return False
        elif (lst[2] == lst[3]): # third and fourth digits can't be the same
            return False
        elif (lst[1] == 0): # second digit can't be zero
            return False
        else:
            return True
        
# Checks if a price works in Side by Side
def compatible_for_sidebyside(price):
    p = int(price)
    if (p > 9999): # make sure the price is less than $10,000
        return False
    else:
        lst = [int(i) for i in str(p)] # put each digit into a list
        if (lst[2] == 0): # third digit can't be zero
            return False
        elif ( (lst[0] == lst[2]) and (lst[1] == lst[3]) ): # can't have a price with digits XYXY (e.g. 4242)
            return False
        else:
            return True

# Check Game
def play_checkgame():
    items = [] # generate the item database
    file = dir_path + larg_path # generate the filepath to the item bank
    print("\nCHECK GAME")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        if (int(Large(*line.split()).price) < 8000):
            items.append(Large(*line.split()))

    size = len(items) # get the size of the item bank
    prize_id = randrange(size) # pick a prize ID
    prize = Large(items[prize_id].description, items[prize_id].shortname, items[prize_id].price) # pick the prize with the chosen ID

    print(prize.showPrize()) # show the prize
    print() # line break

    print("AT LEAST $8,000 BUT NOT OVER $9,000")

    # enter the value of the check
    signing = True
    while signing:
        value = input("How much will you write the check for?: $")
        try:
            value = int(value)
        except ValueError:
            continue
        else:
            signing = False

    # results
    input("\nYou wrote the check for $" + str(value) + " ")
    print("The actual retail price of the prize is " + prize.showARP())
    total = int(value) + int(prize.price) # get total
    print("For a total of $" + str(total))
    if (8000 <= total <= 9000):
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose.")
    endgame()

# Coming or Going
def play_comingorgoing():
    items = [] # generate the item database
    file = dir_path + larg_path # generate the filepath to the item bank
    print("\nCOMING OR GOING")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        if (compatible_for_cog(Large(*line.split()).price)):
            items.append(Large(*line.split()))

    size = len(items) # get the size of the item bank
    prize_id = randrange(size) # pick a prize ID
    prize = Large(items[prize_id].description, items[prize_id].shortname, items[prize_id].price) # pick the prize with the chosen ID

    digits = [int(i) for i in str(prize.price)] # put each digit into a list

    # if position is 0, the correct answer will be COMING. If 1, the correct answer will be GOING.
    position = randrange(2)

    print(prize.showPrize()) # show the prize
    print() # line break

    if (position == 0):
        print("1. COMING - " + prize.showARP())
        print("2. GOING - $" + str(digits[3]) + str(digits[2]) + str(digits[1]) + str(digits[0]))
    else:
        print("1. COMING - $" + str(digits[3]) + str(digits[2]) + str(digits[1]) + str(digits[0]))
        print("2. GOING - " + prize.showARP())

    # select the price, ensuring proper input
    choosing = True
    while choosing:
        player_choice = input("Are you coming (1) or going (2)?: ")
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

# Double Prices
def play_doubleprices():
    items = [] # generate the item database
    file = dir_path + larg_path # generate the filepath to the item bank
    print("\nDOUBLE PRICES")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        items.append(Large(*line.split()))

    size = len(items) # get the size of the item bank
    prize_id = randrange(size) # pick a prize ID
    prize = Large(items[prize_id].description, items[prize_id].shortname, items[prize_id].price) # pick the prize with the chosen ID

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

    # select the price, ensuring proper input
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

# Flip Flop
def play_flipflop():
    items = [] # generate the item database
    file = dir_path + larg_path # generate the filepath to the item bank
    print("\nFLIP FLOP")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        if (compatible_for_flipflop(Large(*line.split()).price)):
            items.append(Large(*line.split()))

    size = len(items) # get the size of the item bank
    prize_id = randrange(size) # pick a prize ID
    prize = Large(items[prize_id].description, items[prize_id].shortname, items[prize_id].price) # pick the prize with the chosen ID

    digits = [int(i) for i in str(prize.price)] # put each digit into a list  
    
    # if 0, then FLIP. If 1, then FLOP. If 2, then FLIP-FLOP.
    todo = randrange(3)

    # generate the price options
    if (todo == 0): # FLIP is the correct answer
        wrongPrice = digits[1]*1000 + digits[0]*100 + digits[2]*10 + digits[3]
        flipPrice = int(prize.price)
        flopPrice = digits[1]*1000 + digits[0]*100 + digits[3]*10 + digits[2]
        flipFlopPrice = digits[0]*1000 + digits[1]*100 + digits[3]*10 + digits[2]
    elif (todo == 1): # FLOP is the correct answer
        wrongPrice = digits[0]*1000 + digits[1]*100 + digits[3]*10 + digits[2]
        flipPrice = digits[1]*1000 + digits[0]*100 + digits[3]*10 + digits[2]
        flopPrice = int(prize.price)
        flipFlopPrice = digits[1]*1000 + digits[0]*100 + digits[2]*10 + digits[3]
    else: # FLIP-FLOP is the correct answer
        wrongPrice = digits[1]*1000 + digits[0]*100 + digits[3]*10 + digits[2]
        flipPrice = digits[0]*1000 + digits[1]*100 + digits[3]*10 + digits[2]
        flopPrice = digits[1]*1000 + digits[0]*100 + digits[2]*10 + digits[3]
        flipFlopPrice = int(prize.price)

    print(prize.showPrize()) # show the prize
    print() # line break

    print("The price is not $" + str(wrongPrice) + ".")
    print("But you can FLIP (1) and make it $" + str(flipPrice))
    print("Or you can FLOP (2) and make it $" + str(flopPrice))
    print("Or you can FLIP-FLOP (3) and make it $" + str(flipFlopPrice))

    # select the price, ensuring proper input
    choosing = True
    while choosing:
        player_choice = input("Which would you like to do?: ")
        try:
            player_choice = int(player_choice)
        except ValueError:
            continue
        if ( (player_choice >= 1) and (player_choice <= 3) ):
            choosing = False

    print("The actual retail price is " + prize.showARP())

    if (player_choice == todo+1):
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose.")

    endgame()

# Side by Side
def play_sidebyside():
    items = [] # generate the item database
    file = dir_path + larg_path # generate the filepath to the item bank
    print("\nSIDE BY SIDE")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        if (compatible_for_sidebyside(Large(*line.split()).price)):
            items.append(Large(*line.split()))

    size = len(items) # get the size of the item bank
    prize_id = randrange(size) # pick a prize ID
    prize = Large(items[prize_id].description, items[prize_id].shortname, items[prize_id].price) # pick the prize with the chosen ID

    digits = [int(i) for i in str(prize.price)] # put each digit into a list

    # if position is 0, the digits go on the left; if 1, the digits go on the right
    position = randrange(2)

    print(prize.showPrize()) # show the prize
    print() # line break
    if (position == 0):
        print("*" + str(digits[0]) + str(digits[1]) + "*") # digits go on
        print("*" + str(digits[2]) + str(digits[3]) + "*") #  the left
        print("1. LEFT - " + prize.showARP() ) # correct price
        print("2. RIGHT - $" + str(digits[2]) + str(digits[3]) + str(digits[0]) + str(digits[1])) # wrong price
    else:
        print("*" + str(digits[2]) + str(digits[3]) + "*") # digits go on
        print("*" + str(digits[0]) + str(digits[1]) + "*") #  the right
        print("1. LEFT - $" + str(digits[2]) + str(digits[3]) + str(digits[0]) + str(digits[1])) # wrong price
        print("2. RIGHT - " + prize.showARP() ) # correct price

    # select the price, ensuring proper input
    choosing = True
    while choosing:
        player_choice = input("On which side (1-2) do the digits go?: ")
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