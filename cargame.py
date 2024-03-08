from prize import *
from random import randrange
import random

def has_zeros(price):
    p = int(price)
    flag = False # checks for zeros
    lst = [int(i) for i in str(p)] # put each digit into a list
    for x in lst:
        if (x == 0):
            flag = True
    if (flag):
        return True
    else:
        return False
    
# makes sure that a car's first two digits and last two digits are not the same
def incompatible_moneygame(price):
    p = int(price)
    lst = [int(i) for i in str(p)] # put each digit into a list
    if ( (lst[0] == lst[3]) and (lst[1] == lst[4]) ):
        return True
    else:
        return False
    
# makes a single-digit number have a 0 before it
def mgspace(value):
    v = int(value)
    if (v < 10):
        return str("0" + str(v))
    else:
        return str(v)

# Lucky $even
def play_luckyseven():
    items = [] # generate the item database
    file = dir_path + car_path # generate the filepath to the item bank
    print("\nLUCKY $EVEN")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract only car prices without zeros and prices less than max_car_price
        if ( (not has_zeros(Car(*line.split()).price)) and ( int(Car(*line.split()).price) < max_car_price) ):
            items.append(Car(*line.split()))

    size = len(items) # get the size of the item bank
    prize_id = randrange(size) # pick a prize ID
    car = Car(items[prize_id].model, items[prize_id].options, items[prize_id].price)

    digits = [int(i) for i in str(car.price)] # put each digit into a list
    dollars = 7 # the player starts with $7
    won = False # Determines if the player has been revealed
    on = 0 # Current digit

    print(car.showModel())
    print("Comes with: " + car.showOptions())

    while ( (dollars > 0) and (not won) ):
        print("Dollars left: $" + str(dollars)) # show money left
        
        # show revealed digits
        if (on == 4):
            print("$" + str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3]) + str(digits[4]))
        elif (on == 3):
            print("$" + str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3]) + "*")
        elif (on == 2):
            print("$" + str(digits[0]) + str(digits[1]) + str(digits[2]) +  "**")
        elif (on == 1):
            print("$" + str(digits[0]) + str(digits[1]) + "***")
        else:
            print("$" + str(digits[0]) + "****")

        # Entering a digit
        entry = True
        while entry:
            player_choice = input("What is the next digit (1-9)?: ")
            try:
                player_choice = int(player_choice)
            except ValueError:
                continue
            if (1 <= player_choice <= 9):
                entry = False

        if (on < 5): # subtract the difference between the player's input and the actual number
            dollars -= abs(digits[on+1] - player_choice)
            on += 1
        
        if ( (on >= 4) and (dollars >= 1) ):
            won = True
        # end while loop

    if (dollars <= 0):
        print("Sorry, you lose.")
        print("The price of the car was " + car.showARP() + ".")
    else:
        print("Price: " + car.showARP())
        print("Congratulations, you win!")

    endgame()

# Money Game
def play_moneygame():
    items = [] # generate the item database
    file = dir_path + car_path # generate the filepath to the item bank
    print("\nMONEY GAME")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract only Money Game-compatible car prices and prices less than max_car_price
        if ( (not has_zeros(Car(*line.split()).price)) and ( int(Car(*line.split()).price) < max_car_price) ):
            items.append(Car(*line.split()))

    size = len(items) # get the size of the item bank
    prize_id = randrange(size) # pick a prize ID
    car = Car(items[prize_id].model, items[prize_id].options, items[prize_id].price)

    spaces = [] # numbers on the board
    digits = [int(i) for i in str(car.price)] # put each digit into a list
    front_digits = digits[0]*10 + digits[1] # front of the car
    back_digits = digits[3]*10 + digits[4] # back of the car
    which_front = randrange(3) # determines the other decoy front values

    # start appending to spaces
    spaces.append(front_digits)
    if (which_front == 0):
        first = front_digits+1
        second = front_digits+2
    elif (which_front == 1):
        first = front_digits-1
        second = front_digits+1
    else:
        first = front_digits-1
        second = front_digits-2
    
    # append the two decoy values
    spaces.append(first)
    spaces.append(second)

    # ensure that the decoy values aren't equal to the back digits
    if (spaces[1] == back_digits):
        while ( (spaces[1] == front_digits) or (spaces[1] == back_digits) ):
            spaces[1] = randrange(100) # random value between 00 and 99
    if (spaces[2] == back_digits):
          while ( (spaces[2] == front_digits) or (spaces[2] == back_digits) or (spaces[2] == spaces[1]) ):
            spaces[2] = randrange(100) # random value between 00 and 99

    # place the back of the car plus the remaining spaces up to spaces[8]
    spaces.append(back_digits)  # start with the back of the car (spaces[3])
    temp = spaces[0] # temp will be used as a temporary variable throughout
    while ( (temp == spaces[0]) or (temp == spaces[1]) or (temp == spaces[2]) or (temp == spaces[3]) ):
        temp = randrange(100)
    spaces.append(temp) # add spaces[4]

    while ( (temp == spaces[0]) or (temp == spaces[1]) or (temp == spaces[2]) or (temp == spaces[3]) or (temp == spaces[4]) ):
        temp = randrange(100) 
    spaces.append(temp) # add spaces[5]

    while ( (temp == spaces[0]) or (temp == spaces[1]) or (temp == spaces[2]) or (temp == spaces[3]) or (temp == spaces[4]) or (temp == spaces[5]) ):
        temp = randrange(100)
    spaces.append(temp) # add spaces[6]

    while ( (temp == spaces[0]) or (temp == spaces[1]) or (temp == spaces[2]) or (temp == spaces[3]) or (temp == spaces[4]) or (temp == spaces[5]) or (temp == spaces[6]) ):
        temp = randrange(100)
    spaces.append(temp) # add spaces[7]  

    while ( (temp == spaces[0]) or (temp == spaces[1]) or (temp == spaces[2]) or (temp == spaces[3]) or (temp == spaces[4]) or (temp == spaces[5]) or (temp == spaces[6] ) or (temp == spaces[7]) ):
        temp = randrange(100)
    spaces.append(temp) # add spaces[8]

    random.shuffle(spaces) # shuffle the spaces

    picked = [False, False, False, False, False, False, False, False, False] # determines if each space has been chosen
    won = False
    lost = False
    found_front = False
    found_back = False
    money_earned = 0 # total money the player has accumulated
    amts_picked = 0 # money cards the player has chosen

    # strings that denote each space
    s = ["XX", "XX", "XX", "XX", "XX", "XX", "XX", "XX", "XX"]
    s[0] = mgspace(spaces[0]) # top-left
    s[1] = mgspace(spaces[1]) # top-center
    s[2] = mgspace(spaces[2]) # top-right
    s[3] = mgspace(spaces[3]) # center-left
    s[4] = mgspace(spaces[4]) # center
    s[5] = mgspace(spaces[5]) # center-right
    s[6] = mgspace(spaces[6]) # bottom-left
    s[7] = mgspace(spaces[7]) # bottom-center
    s[8] = mgspace(spaces[8]) # bottom-right

    print(car.showModel())
    print("Comes with: " + car.showOptions())

    while (not won and not lost):
        chosen_space = 9 # this determines the space the player picked; 9 is a placeholder value
        print() # line break
        print("---------------------")
        print("A. " + s[0] + " | B. " + s[1] + " | C. " + s[2])
        print("D. " + s[3] + " | E. " + s[4] + " | F. " + s[5])
        print("G. " + s[6] + " | H. " + s[7] + " | I. " + s[8])
        if ( (not found_front) and (not found_back) ):
            print("-------$**" + str(digits[2]) + "**--------")
        elif ( (found_front) and (not found_back) ):
            print("-------$" + str(front_digits) + str(digits[2]) + "**--------")
        elif ( (not found_front) and (found_back) ):
            print("-------$**" + str(digits[2]) + str(back_digits) + "--------")
        
        # choose a space on the board
        choosing = True
        while choosing:
            player_choice = input("Which space (enter the letter) do you want to pick?: ")
            if ( (player_choice == "A") or (player_choice == "a") ): # top-left
                if (not picked[0]):
                    picked[0] = True
                    chosen_space = 0
                    choosing = False
                    valid = True
            elif ( (player_choice == "B") or (player_choice == "b") ): # top-center
                if (not picked[1]):
                    picked[1] = True
                    chosen_space = 1
                    choosing = False
                    valid = True
            elif ( (player_choice == "C") or (player_choice == "c") ): # top-right
                if (not picked[2]):
                    picked[2] = True
                    chosen_space = 2
                    choosing = False
                    valid = True
            elif ( (player_choice == "D") or (player_choice == "d") ): # center-left
                if (not picked[3]):
                    picked[3] = True
                    chosen_space = 3
                    choosing = False
                    valid = True
            elif ( (player_choice == "E") or (player_choice == "e") ): # center
                if (not picked[4]):
                    picked[4] = True
                    chosen_space = 4
                    choosing = False
                    valid = True
            elif ( (player_choice == "F") or (player_choice == "f") ): # center-right
                if (not picked[5]):
                    picked[5] = True
                    chosen_space = 5
                    choosing = False
                    valid = True
            elif ( (player_choice == "G") or (player_choice == "g") ): # bottom-left
                if (not picked[6]):
                    picked[6] = True
                    chosen_space = 6
                    choosing = False
                    valid = True
            elif ( (player_choice == "H") or (player_choice == "h") ): # bottom-center
                if (not picked[7]):
                    picked[7] = True
                    chosen_space = 7
                    choosing = False
                    valid = True
            elif ( (player_choice == "I") or (player_choice == "i") ): # bottom-right
                if (not picked[8]):
                    picked[8] = True
                    chosen_space = 8
                    choosing = False
                    valid = True
            else:
                pass

            # what happens if the player picks a space
            if (valid):
                print("Let's see what's behind this space...")
                if (spaces[chosen_space] == front_digits):
                    print("You found the front of the car!")
                    s[chosen_space] = "FF"
                    found_front = True
                elif (spaces[chosen_space] == back_digits):
                    print("You found the back of the car!")
                    s[chosen_space] = "BB"
                    found_back = True
                else:
                    print("There's cash behind this space.")
                    s[chosen_space] = "$$"
                    money_earned += spaces[chosen_space]
                    amts_picked += 1
                valid = False

            # win/loss conditions
            if (found_front and found_back):
                won = True
            elif ( (amts_picked >= 4) and (not won) ):
                lost = True

    # results
    print() # line break
    print(car.showARP())
    if won:
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose. At least you won $" + str(money_earned) + ".")

    endgame()

# That's Too Much!
def play_thatstoomuch():
    items = [] # generate the item database
    file = dir_path + car_path # generate the filepath to the item bank
    print("\nTHAT'S TOO MUCH!")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract only car prices without zeros and prices less than max_car_price
        if ( (not has_zeros(Car(*line.split()).price)) and ( int(Car(*line.split()).price) < max_car_price) ):
            items.append(Car(*line.split()))

    size = len(items) # get the size of the item bank
    prize_id = randrange(size) # pick a prize ID
    car = Car(items[prize_id].model, items[prize_id].options, items[prize_id].price)
    price = int(car.price)
    
    # gameplay stuff
    prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # row of prices with placeholder values
    too_much = price + randrange(500, 1500) # the first price above the ARP
    too_much_pos = randrange(6) # random space from 3 to 8

    # initialize the price list
    if (too_much_pos == 0): # third price is the first "TOO MUCH" price
        prices[2] = too_much
        prices[1] = too_much - randrange(500, 1500)
        while (prices[1] >= price):
            prices[1] = too_much - randrange(500, 1500)
        prices[0] = prices[1] - randrange(500, 1500)
        prices[3] = too_much + randrange(500, 1500)
        prices[4] = prices[3] + randrange(500, 1500)
        prices[5] = prices[4] + randrange(500, 1500)
        prices[6] = prices[5] + randrange(500, 1500)
        prices[7] = prices[6] + randrange(500, 1500)
        prices[8] = prices[7] + randrange(500, 1500)
        prices[9] = prices[8] + randrange(500, 1500)
    elif (too_much_pos == 1): # fourth price is the first "TOO MUCH" price
        prices[3] = too_much
        prices[2] = too_much - randrange(500, 1500)
        while (prices[2] >= price):
            prices[2] = too_much - randrange(500, 1500)
        prices[1] = prices[2] - randrange(500, 1500)
        prices[0] = prices[1] - randrange(500, 1500)
        prices[4] = too_much + randrange(500, 1500)
        prices[5] = prices[4] + randrange(500, 1500)
        prices[6] = prices[5] + randrange(500, 1500)
        prices[7] = prices[6] + randrange(500, 1500)
        prices[8] = prices[7] + randrange(500, 1500)
        prices[9] = prices[8] + randrange(500, 1500)
    elif (too_much_pos == 2): # fifth price is the first "TOO MUCH" price
        prices[4] = too_much
        prices[3] = too_much - randrange(500, 1500)
        while (prices[3] >= price):
            prices[3] = too_much - randrange(500, 1500)
        prices[2] = prices[3] - randrange(500, 1500)
        prices[1] = prices[2] - randrange(500, 1500)
        prices[0] = prices[1] - randrange(500, 1500)
        prices[5] = too_much + randrange(500, 1500)
        prices[6] = prices[5] + randrange(500, 1500)
        prices[7] = prices[6] + randrange(500, 1500)
        prices[8] = prices[7] + randrange(500, 1500)
        prices[9] = prices[8] + randrange(500, 1500)
    elif (too_much_pos == 3): # sixth price is the first "TOO MUCH" price
        prices[5] = too_much
        prices[4] = too_much - randrange(500, 1500)
        while (prices[4] >= price):
            prices[4] = too_much - randrange(500, 1500)
        prices[3] = prices[4] - randrange(500, 1500)
        prices[2] = prices[3] - randrange(500, 1500)
        prices[1] = prices[2] - randrange(500, 1500)
        prices[0] = prices[1] - randrange(500, 1500)
        prices[6] = too_much + randrange(500, 1500)
        prices[7] = prices[6] + randrange(500, 1500)
        prices[8] = prices[7] + randrange(500, 1500)
        prices[9] = prices[8] + randrange(500, 1500)
    elif (too_much_pos == 4): # seventh price is the first "TOO MUCH" price
        prices[6] = too_much
        prices[5] = too_much - randrange(500, 1500)
        while (prices[5] >= price):
            prices[5] = too_much - randrange(500, 1500)
        prices[4] = prices[5] - randrange(500, 1500)
        prices[3] = prices[4] - randrange(500, 1500)
        prices[2] = prices[3] - randrange(500, 1500)
        prices[1] = prices[2] - randrange(500, 1500)
        prices[0] = prices[1] - randrange(500, 1500)
        prices[7] = too_much + randrange(500, 1500)
        prices[8] = prices[7] + randrange(500, 1500)
        prices[9] = prices[8] + randrange(500, 1500)
    else:   # eighth price is the first "TOO MUCH" price
        prices[7] = too_much
        prices[6] = too_much - randrange(500, 1500)
        while (prices[6] >= price):
            prices[6] = too_much - randrange(500, 1500)
        prices[5] = prices[6] - randrange(500, 1500)
        prices[4] = prices[5] - randrange(500, 1500)
        prices[3] = prices[4] - randrange(500, 1500)
        prices[2] = prices[3] - randrange(500, 1500)
        prices[1] = prices[2] - randrange(500, 1500)
        prices[0] = prices[1] - randrange(500, 1500)
        prices[8] = too_much + randrange(500, 1500)
        prices[9] = prices[8] + randrange(500, 1500)

    on = 0 # price the player is on
    stop = False
    keep_going = False

    print(car.showModel())
    print("Comes with: " + car.showOptions())

    # start gameplay
    while ( (on < 9) and (not stop) ):
        print() # line break
        print(str(on+1) + ". $" + str(prices[on]))
        choosing = True
        while (choosing):
            player_choice = input("Keep going (Y) or THAT'S TOO MUCH (N)?: ")
            if ( (player_choice == "Y") or (player_choice == "y")):
                keep_going = True
                choosing = False
            elif ( (player_choice == "N") or (player_choice == "n")):
                choosing = False
                stop = True
            else:
                pass
            if (keep_going):
                on += 1
                keep_going = False

    print() # line break
    if (on == 9):
        print("10. $" + str(prices[9]))
        print("THAT'S TOO MUCH!")
    else:
        print("THAT'S TOO MUCH!")

    # results
    print() # line break
    print("The actual retail price of the car is " + car.showARP())
    if ( (on - 2) == too_much_pos):
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose.")

    endgame()  
 