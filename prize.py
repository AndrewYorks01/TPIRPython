def fix(string):
    return string.replace("_", " ")

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
    
