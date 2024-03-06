from prize import *
from random import randrange
import random

# Bargain Game
def play_bargaingame():
    all_items = [] # generate the item database
    file = dir_path + med_path # generate the filepath to the item bank
    print("\nBARGAIN GAME")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        if (int(Medium(*line.split()).price) > 1600):
            all_items.append(Medium(*line.split()))

    size = len(all_items) # get the size of the item bank
    ids = random.sample(range(0, size), 2) # pick two different item IDs
    items = [] # generate the items

    # set all the items
    for number in range (0, 2):
       item = Medium(all_items[ids[number]].description, all_items[ids[number]].shortname, all_items[ids[number]].price)
       items.append(item)

    # if 0, the prize on the left is the bigger bargain; if 1, the prize on the right is
    bigger_bargain = randrange(2)
    bargain1 = random.randint(3, 7) * 100
    bargain2 = random.randint(8, 12) * 100

    if (bigger_bargain == 0):
        difference1 = int(items[0].price) - bargain2
        difference2 = int(items[1].price) - bargain1
    else:
        difference1 = int(items[0].price) - bargain1
        difference2 = int(items[1].price) - bargain2

    # show setup
    print("1. " + items[0].showPrize() + " - $" + str(difference1))
    print("2. " + items[1].showPrize() + " - $" + str(difference2))
    print() # line break

    # select an item, ensuring proper input
    choosing = True
    while (choosing):
        player_choice = input("Which price (enter the number) is the bigger bargain?: ")
        try:
            player_choice = int(player_choice)
        except ValueError:
            continue
        if ( (player_choice == 1) or (player_choice == 2) ):
            choosing = False

    # set ID of item that the player didn't choose
    if (player_choice == 1):
        id = int(1)
        if (bigger_bargain == 0):
            dif_fir = bargain1
            dif_sec = bargain2
        else:
            dif_fir = bargain2
            dif_sec = bargain1
    else:
        id = int(0)
        if (bigger_bargain == 0):
            dif_fir = bargain2
            dif_sec = bargain1
        else:
            dif_fir = bargain1
            dif_sec = bargain2

    print() # line break
    print("The actual retail price of the " + items[id].showShortName() + " is " + items[id].showARP())
    input("For a difference of $" + str(dif_fir) + " ")
    print("\nThe actual retail price of the " + items[player_choice-1].showShortName() + " is " + items[player_choice-1].showARP())
    print("For a difference of $" + str(dif_sec))
    if (bigger_bargain == player_choice-1):
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose.")

    endgame()


# Clock Game
def play_clockgame():
    all_items = [] # generate the item database
    file = dir_path + med_path # generate the filepath to the item bank
    print("\nCLOCK GAME")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        if (int(Medium(*line.split()).price) < 1000):
            all_items.append(Medium(*line.split()))

    size = len(all_items) # get the size of the item bank
    ids = random.sample(range(0, size), 2) # pick two different item IDs
    items = [] # generate the items

    # set all the items
    for number in range (0, 2):
       item = Medium(all_items[ids[number]].description, all_items[ids[number]].shortname, all_items[ids[number]].price)
       items.append(item)

    chances = 45 # instead of a clock, the player will have 45 chances
    won1 = False # determines if the player has won the first prize
    won2 = False # determines if the player has won the second prize

    # display the two prizes
    print("1. " + items[0].showPrize())
    print("2. " + items[1].showPrize())

    while ( (chances > 0 ) and (not won1) ):
        print("Chances left: " + str(chances))
        bidding = True
        while (bidding):
            bid = input("Your bid on the " + items[0].showShortName() + ": $")
            try:
                bid = int(bid)
            except ValueError:
                continue
            else:
                bidding = False
        if (bid == int(items[0].price)): # guessed correctly
            won1 = True
        elif (int(items[0].price) > bid): # HIGHER
            print("HIGHER")
            chances -= 1
        else:   # LOWER
            print("LOWER")
            chances -= 1

    if (won1): # message if player won first prize
        print("You got it! On to the next item...\n")

    while ( (chances > 0) and (won1) and (not won2) ):
        print("Chances left: " + str(chances))
        bidding = True
        while (bidding):
            bid = input("Your bid on the " + items[1].showShortName() + ": $")
            try:
                bid = int(bid)
            except ValueError:
                continue
            else:
                bidding = False
        if (bid == int(items[1].price)): # guessed correctly
            won2 = True
        elif (int(items[1].price) > bid): # HIGHER
            print("HIGHER")
            chances -= 1
        else:   # LOWER
            print("LOWER")
            chances -= 1

    # results
    if (won1 and won2): # won both prizes
        print("\nCongratulations, you win both prizes!")
    elif (won1 and not won2): # won first prize
        print("\nWell, at least you won the " + items[0].showShortName() + ".")
    else:
        print("\nSorry, you lose.")

    endgame()

# Do the Math
def play_dothemath():
    all_items = [] # generate the item database
    file = dir_path + med_path # generate the filepath to the item bank
    print("\nDO THE MATH")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        if (int(Medium(*line.split()).price) >= 1000):
            all_items.append(Medium(*line.split()))

    size = len(all_items) # get the size of the item bank
    items = [] # generate the items

    # create a setup
    setup = False
    while (not setup):
      ids = random.sample(range(0, size), 2) # pick two different item IDs
      first = ids[0]
      second = ids[1]
      # hold items
      temp1 = Medium(all_items[first].description, all_items[first].shortname, all_items[first].price)
      temp2 = Medium(all_items[second].description, all_items[second].shortname, all_items[second].price)
      # hold prices
      tprice1 = int(all_items[first].price)
      tprice2 = int(all_items[second].price)
      if ( ((abs(tprice1 - tprice2 )) >= 100) ):
          items.append(temp1)
          items.append(temp2)
          setup = True

    # cash bonus
    middle = abs(tprice1 - tprice2)

    # determines what the correct operation will be (if 0, PLUS, if 1, MINUS)
    if (tprice1 < tprice2):
        operation = 0
    else:
        operation = 1
    
    # show the prizes
    print("1. " + items[0].showPrize())
    print("2. " + items[1].showPrize())
    print() # line break
    print("1. " + items[0].showShortName() + " + $" + str(middle) + " = " + items[1].showShortName())
    print("2. " + items[0].showShortName() + " - $" + str(middle) + " = " + items[1].showShortName())

    # select an equation, ensuring proper input
    choosing = True
    while (choosing):
        player_choice = input("Which equation (enter the number) is correct?: ")
        try:
            player_choice = int(player_choice)
        except ValueError:
            continue
        if ( (player_choice == 1) or (player_choice == 2) ):
            choosing = False

    print() # line break
    input("The actual retail price of the " + items[0].showShortName() + " is " + items[0].showARP())
    print("The actual retail price of the " + items[1].showShortName() + " is " + items[1].showARP())
    if (player_choice-1 == operation):
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose.")

    endgame()  

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
    ids = random.sample(range(0, size), 3) # pick three different item IDs
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

# One Right Price
def play_onerightprice():
    all_items = [] # generate the item database
    file = dir_path + med_path # generate the filepath to the item bank
    print("\nONE RIGHT PRICE")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        if (int(Medium(*line.split()).price) >= 1000):
            all_items.append(Medium(*line.split()))

    size = len(all_items) # get the size of the item bank
    items = [] # generate the items

    # create a setup
    setup = False
    while (not setup):
      ids = random.sample(range(0, size), 2) # pick two different item IDs
      first = ids[0]
      second = ids[1]
      # hold items
      temp1 = Medium(all_items[first].description, all_items[first].shortname, all_items[first].price)
      temp2 = Medium(all_items[second].description, all_items[second].shortname, all_items[second].price)
      # hold prices
      tprice1 = int(all_items[first].price)
      tprice2 = int(all_items[second].price)
      if ( ((abs(tprice1 - tprice2 )) >= 100) ):
          items.append(temp1)
          items.append(temp2)
          setup = True

    right_id = randrange(2) # ID of the item with the right price
    right_price = int(items[right_id].price) # set the one right price

    # Gameplay
    print() # line break
    print("One right price: $" + str(right_price))
    print("1. " + items[0].showPrize())
    print("2. " + items[1].showPrize())

    # make a choice, ensuring proper input
    choosing = True
    while (choosing):
        player_choice = input("Which prize (enter the number) has the one right price?: ")
        try:
            player_choice = int(player_choice)
        except ValueError:
            continue
        if ( (player_choice == 1) or (player_choice == 2) ):
            choosing = False

    # results
    print() # line break
    print("The actual retail price of the " + items[player_choice-1].showShortName() + " is " + items[player_choice-1].showARP())
    if (int(items[player_choice-1].price) == right_price):
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
    ids = random.sample(range(0, size), 3) # pick three different item IDs
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

# Shopping Spree
def play_shoppingspree():
    all_items = [] # generate the item database
    file = dir_path + med_path # generate the filepath to the item bank
    print("\nSHOPPING SPREE")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        all_items.append(Medium(*line.split()))

    size = len(all_items) # get the size of the item bank
    ids = random.sample(range(0, size), 4) # pick three different item IDs
    items = [] # generate the items

    # set all the items
    for number in range (0, 4):
       item = Medium(all_items[ids[number]].description, all_items[ids[number]].shortname, all_items[ids[number]].price)
       items.append(item)

    # set gameplay stuff
    spent_so_far = 0 # how much the player has spent
    bought = [False, False, False, False] # determines which items the player has bought
    picks = 0 # items the palyer has chosen

    # calculate the minimum amount 
    temps = [int(items[0].price), int(items[1].price), int(items[2].price), int(items[3].price)] # prices of each item
    temps.sort() # sort from smallest to largest

    # to calculate the minimum amount, take the values of the three most expensive items
    # and round it down to the nearest hundred.
    spending_amt = temps[1] + temps[2] + temps[3]
    round_off = spending_amt % 100
    spending_amt -= round_off

    # begin gameplay
    while (picks < 3):
        # show the items
        for p in range (0, 4):
            if (bought[p]):
                print(str(p+1) + ". " + items[p].showPrize() + " - " + items[p].showARP())
            else:
                print(str(p+1) + ". " + items[p].showPrize())
        print("Spending amount: $" + str(spending_amt))
        print("Left to spend: $" + str(spending_amt - spent_so_far))
        # pick an item
        selecting = True
        while (selecting):
            player_choice = input("Which item (enter the number) would you like to buy?: ")
            try:
                player_choice = int(player_choice)
            except ValueError: # not an int
                continue
            if ( (player_choice < 1) or (player_choice > 4) ): # not between 1 and 4
                pass
            elif (bought[player_choice - 1]): # already purchased the item
                pass
            else:
                selecting = False
        
        print() # line break
        print("The actual retail price of the " + items[player_choice-1].showShortName() + " is " + items[player_choice-1].showARP())
        bought[player_choice-1] = True
        spent_so_far += int(items[player_choice-1].price) 
        picks += 1
        print() # line break

    # results
    print("Spending amount: $" + str(spending_amt))
    print("Spent so far: $" + str(spent_so_far))
    print() # line break
    if (spent_so_far >= spending_amt):
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose.")
    
    endgame()

# Switch?
def play_switch():
    all_items = [] # generate the item database
    file = dir_path + med_path # generate the filepath to the item bank
    print("\nSWITCH?")

    lines = open(file).readlines() # open the item bank
    for line in lines: # extract the items from the text file into the database
        if (int(Medium(*line.split()).price) >= 1000):
            all_items.append(Medium(*line.split()))

    size = len(all_items) # get the size of the item bank
    items = [] # generate the items

    # create a setup
    setup = False
    while (not setup):
      ids = random.sample(range(0, size), 2) # pick two different item IDs
      first = ids[0]
      second = ids[1]
      # hold items
      temp1 = Medium(all_items[first].description, all_items[first].shortname, all_items[first].price)
      temp2 = Medium(all_items[second].description, all_items[second].shortname, all_items[second].price)
      # hold prices
      tprice1 = int(all_items[first].price)
      tprice2 = int(all_items[second].price)
      if ( ((abs(tprice1 - tprice2 )) >= 100) ):
          items.append(temp1)
          items.append(temp2)
          setup = True

    # if 0, the prices stay where they are. if 1, the prices should be switched.
    to_switch = randrange(2)

    if (to_switch == 0):
        print("1. " + items[0].showPrize() + " - " + items[0].showARP())
        print("2. " + items[1].showPrize() + " - " + items[1].showARP())
    else:
        print("1. " + items[0].showPrize() + " - " + items[1].showARP())
        print("2. " + items[1].showPrize() + " - " + items[0].showARP())

    # make a choice, ensuring proper input
    choosing = True
    while (choosing):
        player_choice = input("Are these prices correct (1) or should they be switched (2)?: ")
        try:
            player_choice = int(player_choice)
        except ValueError:
            continue
        if ( (player_choice == 1) or (player_choice == 2) ):
            choosing = False

    # results
    print() # line break
    print("The actual retail price of the " + items[0].showShortName() + " is " + items[0].showARP())
    print("The actual retail price of the " + items[1].showShortName() + " is " + items[1].showARP())

    if (player_choice-1 == to_switch):
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose.")     

    endgame()