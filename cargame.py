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
