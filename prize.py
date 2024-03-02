import os
import pathlib

# Paths to the prize banks.
dir_path = str(pathlib.Path(__file__).parent.resolve())
groc_path = "\prizes\grocery.txt"

def endgame():
    input("Press any key to continue: ")
    os.system('cls') # clear the screen  

# Replaces underscores in the input file with spaces.
def fix(string):
    return string.replace("_", " ")

# A grocery item
class Grocery:
    def __init__(self, description, shortname, price):
        self.description = description
        self.shortname = shortname
        self.price = price

    def showPrize(self):
        return str(fix(self.description))

    def showShortName(self):
        return str(fix(self.shortname))

    def showARP(self):
        fl = float(self.price)
        return str(f"${fl:.2f}")

# A small prize
class Small:
    def __init__(self, description, shortname, price):
        self.description = description
        self.shortname = shortname
        self.price = price

    def showPrize(self):
        return fix(self.description)

    def showShortName(self):
        return fix(self.shortname)

    def showARP(self):
        return "$" + self.price

# A medium prize   
class Medium:
    def __init__(self, description, shortname, price):
        self.description = description
        self.shortname = shortname
        self.price = price

    def showPrize(self):
        return fix(self.description)

    def showShortName(self):
        return fix(self.shortname)

    def showARP(self):
        return "$" + self.price

# A large prize   
class Large:
    def __init__(self, description, shortname, price):
        self.description = description
        self.shortname = shortname
        self.price = price

    def showPrize(self):
        return fix(self.description)

    def showShortName(self):
        return fix(self.shortname)

    def showARP(self):
        return "$" + self.price

# A car
class Car:
    def __init__(self, model, options, price):
        self.model = model
        self.options = options
        self.price = price

    def showModel(self):
        return fix(self.model)
    
    def showOptions(self):
        return fix(self.options)
    
    def showARP(self):
        return "$" + self.price
    
