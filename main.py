from prize import *
from grocgame import *
from smallprize import *
from singleprize import *
from multiprize import *
from cargame import *

def display_main_menu():
    print("1. Grocery games")
    print("2. Small prize games")
    print("3. Single-prize games")
    print("4. Multi-prize games")
    print("5. Car games")
    print("6. Car + other item games")
    print("7. Cash games")
    print("8. Retired games (A-J)")
    print("9. Retired games (M-W)")
    print("10. Custom games")
    print("11. Play a line-up you've created")
    print("12. Quit")

def display_groc_menu():
    print("GROCERY GAMES")
    print("1. Bullseye")
    print("2. Check-Out")
    print("3. Grocery Game")
    print("4. Hi-Lo")
    print("5. Now... or Then")
    print("6. Pick-a-Pair")
    print("7. Vend-o-Price")
    print("8. Go back")

def display_small_menu():
    print("SMALL PRIZE GAMES")
    print("1. Back to '72")
    print("2. Bonus Game")
    print("3. Cliff Hangers")
    print("4. Secret \"X\"")
    print("5. Shell Game")
    print("6. Go back")

def display_sing_menu():
    print("SINGLE PRIZE GAMES")
    print("1. Balance Game (2006)  8. Pick-a-Number")
    print("2. Bonkers              9. Push-Over")
    print("3. Check Game           10. Range Game")
    print("4. Coming or Going      11. Side by Side")
    print("5. Double Prices        12. Squeeze Play")
    print("6. Flip Flop            13. Go back")
    print("7. Freeze Frame")

def display_mult_menu():
    print("MULTI PRIZE GAMES")
    print("1. Bargain Game     10. One Wrong Price")
    print("2. Clock Game       11. Race Game")
    print("3. Danger Price     12. Safe Crackers")
    print("4. Do the Math      13. Shopping Spree")
    print("5. Double Cross     14. Swap Meet")
    print("6. Easy as 1-2-3    15. Switch?")
    print("7. Make Your Move   16. Take Two")
    print("8. Most Expensive   17. Two for the Price of One")
    print("9. One Right Price  18. Go back")

def display_cars_menu():
    print("CAR GAMES")
    print("1. Card Game    8. One Away")
    print("2. Cover Up     9. Pocket Change")
    print("3. Dice Game    10. That's Too Much!")
    print("4. Gas Money    11. Three Strikes")
    print("5. Gridlock!    12. Triple Play")
    print("6. Lucky $even  13. Go back")
    print("7. Money Game")

def display_cars2_menu():
    print("CAR/OTHER PRIZES GAMES")
    print("1. Any Number       10. Pathfinder")
    print("2. Five Price Tags  11. Rat Race")
    print("3. Golden Road      12. Spelling Bee")
    print("4. Hole in One      13. Stack the Deck")
    print("5. Let 'em Roll     14. Switcheroo")
    print("6. Line 'em Up      15. Temptation")
    print("7. Master Key       16. Ten Chances")
    print("8. More or Less     17. Go back")
    print("9. Pass the Buck")

def display_cash_menu():
    print("CASH GAMES")
    print("1. Grand Game       6. Plinko")
    print("2. 1/2 Off          7. Punch-a-Bunch")
    print("3. Hot Seat         8. Time Is Money")
    print("4. It's in the Bag  9. To the Penny")
    print("5. Pay the Rent     10. Go back")

def display_retired_menu():
    print("RETIRED GAMES (A-J)")
    print("1. Add 'em Up           10. Finish Line")
    print("2. Balance Game (1984)  11. Fortune Hunter")
    print("3. Bullseye (1972)      12. Gallery Game")
    print("4. Bump                 13. Give or Keep")
    print("5. Buy or Sell          14. Hit Me")
    print("6. Clearance Sale       15. Hurdles")
    print("7. Credit Card          16. It's Optional")
    print("8. Double Bullseye      17. Joker")
    print("9. Double Digits        18. Go back")

def display_retired2_menu():
    print("RETIRED GAMES (M-W)")
    print("1. Magic #          10. Split Decision")
    print("2. Make Your Mark   11. Step Up")
    print("3. Mystery Price    12. $uper Ball!!")
    print("4. On the Nose      13. $uper $aver")
    print("5. On the Spot      14. Telephone Game")
    print("6. Penny Ante       15. The Phone Home Game")
    print("7. Poker Game       16. Trader Bob")
    print("8. Professor Price  17. Walk of Fame")
    print("9. Shower Game      18. Go back")

def display_custom_menu():
    print("CUSTOM GAMES")
    print("1. Big Item Bash")
    print("2. Domino Game")
    print("3. Fill 'er Up")
    print("4. Jam")
    print("5. Master Price")
    print("6. One For All")
    print("7. One Way Or Another")
    print("8. 7Up")
    print("9. Go back")

# Program starts here.
print("THE PRICE IS RIGHT")
#test()

Loop = True
while Loop:
    print()
    display_main_menu()
    inp = input("Select a game classification: ")

    # Grocery games
    if inp == "1":
        GrocLoop = True
        while GrocLoop:
            print()
            display_groc_menu()
            gro = input("Select a pricing game: ")
            if gro == "1":
                os.system('cls')
                play_bullseye()
            elif gro == "2":
                os.system('cls')
                play_checkout()
            elif gro == "3":
                os.system('cls')
                play_grocerygame()
            elif gro == "4":
                os.system('cls')
                play_hilo()
            elif gro == "6":
                os.system('cls')
                play_pickapair()
            elif gro == "7":
                os.system('cls')
                play_vendoprice()
            elif gro == "8":
                GrocLoop = False
                os.system('cls')
            else:
                print("Please enter a number between 1 and 8.")

    # Small prize games
    elif inp == "2":
        SmalLoop = True
        while SmalLoop:
            print()
            display_small_menu()
            sma = input("Select a pricing game: ")
            if sma == "1":
                print("You picked Back to '72")
            elif sma == "2":
                os.system('cls')
                play_bonusgame()
            elif sma == "3":
                os.system('cls')
                play_cliffhangers()
            elif sma == "6":
                SmalLoop = False
                os.system('cls')
            else:
                print("Please enter a number between 1 and 6.")

    # Single prize games
    elif inp == "3":
        SingLoop = True
        while SingLoop:
            print()
            display_sing_menu()
            sng = input("Select a pricing game: ")
            if sng == "1":
                print("You picked Balance Game")
            elif sng == "3":
                os.system('cls')
                play_checkgame()
            elif sng == "4":
                os.system('cls')
                play_comingorgoing()
            elif sng == "5":
                os.system('cls')
                play_doubleprices()
            elif sng == "6":
                os.system('cls')
                play_flipflop()
            elif sng == "11":
                os.system('cls')
                play_sidebyside()
            elif sng == "13":
                SingLoop = False
                os.system('cls')
            else:
                print("Please enter a number between 1 and 13.")

    # Multi prize games
    elif inp == "4":
        MultLoop = True
        while MultLoop:
            print()
            display_mult_menu()
            mul = input("Select a pricing game: ")
            if mul == "1":
                print("You picked Bargain Game")
            elif mul == "2":
                os.system('cls')
                play_clockgame()
            elif mul == "4":
                os.system('cls')
                play_dothemath()
            elif mul == "8":
                os.system('cls')
                play_mostexpensive()
            elif mul == "10":
                os.system('cls')
                play_onewrongprice()
            elif mul == "15":
                os.system('cls')
                play_switch()
            elif mul == "18":
                MultLoop = False
                os.system('cls')
            else:
                print("Please enter a number between 1 and 18.")

    # Car games
    elif inp == "5":
        CarLoop = True
        while CarLoop:
            print()
            display_cars_menu()
            cgs = input("Select a pricing game: ")
            if cgs == "1":
                print("You picked Card Game")
            elif cgs == "6":
                os.system('cls')
                play_luckyseven()
            elif cgs == "13":
                CarLoop = False
                os.system('cls')
            else:
                print("Please enter a number between 1 and 13.")

    # Car/other prizes games
    elif inp == "6":
        Car2Loop = True
        while Car2Loop:
            print()
            display_cars2_menu()
            cms = input("Select a pricing game: ")
            if cms == "1":
                print("You picked Any Number")
            elif cms == "17":
                Car2Loop = False
                os.system('cls')
            else:
                print("Please enter a number between 1 and 17.")

    # Cash games
    elif inp == "7":
        CashLoop = True
        while CashLoop:
            print()
            display_cash_menu()
            csh = input("Select a pricing game: ")
            if csh == "1":
                print("You picked Grand Game")
            elif csh == "10":
                CashLoop = False
                os.system('cls')
            else:
                print("Please enter a number between 1 and 10.")

    # Retired games (A-J)
    elif inp == "8":
        RetLoop = True
        while RetLoop:
            print()
            display_retired_menu()
            ret = input("Select a pricing game: ")
            if ret == "1":
                print("You picked Add 'em Up")
            elif ret == "18":
                RetLoop = False
                os.system('cls')
            else:
                print("Please enter a number between 1 and 18.")

    # Retired games (M-W)
    elif inp == "9":
        Ret2Loop = True
        while Ret2Loop:
            print()
            display_retired2_menu()
            re2 = input("Select a pricing game: ")
            if re2 == "1":
                print("You picked Magic #")
            elif re2 == "18":
                Ret2Loop = False
                os.system('cls')
            else:
                print("Please enter a number between 1 and 18.")

    # Custom games
    elif inp == "10":
        CusLoop = True
        while CusLoop:
            print()
            display_custom_menu()
            cus = input("Select a pricing game: ")
            if cus == "1":
                print("You picked Big Item Bash")
            elif cus == "9":
                CusLoop = False
                os.system('cls')
            else:
                print("Please enter a number between 1 and 9.")

    # Play a random game
    elif inp == "11":
        print("This feature hasn't been added yet.")

    # Exit
    elif inp == "12":
        exit()
    else:
        print("Please enter a number between 1 and 12.")

