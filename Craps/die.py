__author__ = 'Lisbeth Alvarez'


from random import randint

class Die(object):
    def __init__(self, numberOfSides, startingColor = "Bone", startingValue = 1, incrementValue = 1 ):
        self.numberOfSides = numberOfSides
        self.startingColor = startingColor
        self.startingValue = startingValue
        self.incrementValue = incrementValue
        self.value = None

    def __str__(self):
        return str(self.getValue())

    def setValue(selfself, newValue):
        self.value = newValue

    def getValue(self):
        return self.value

    def setNumberOfSides(self, newNumberOfSides):
        self.numberOfSides = newNumberOfSides

    def getNumberOfSides(self):
        return self.numberOfSides

    def setStartingColor(self, newStartingColor):
        self.startingColor = newStartingColor

    def getStartingColor(self):
        return self.startingColor

    def setStartingValue(self, newStartingValue):
        self.startingValue = newStartingValue

    def getStartingValues(self):
        return self.startingValue

    def setIncrementValue(self, newIncrementValue):
        self.incrementValue=newIncrementValue

    def getIncrementValue(self):
        return self.incrementValue

    def roll(self):
        self.value = randint(self.startingValue, (self.numberOfSides - 1) + self.startingValue) * self.incrementValue
        return self.value