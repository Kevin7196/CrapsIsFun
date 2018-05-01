__author__ = 'Lisbeth Alvarez'

from die import Die

class CrapsGame(object):
    def __init__(self):
        self.winsCount = 0
        self.lossesCount = 0
        self.currentBet = 10
        self.startingBank = 1000
        self.currentBank = self.startingBank
        self.currentRoll = 0
        self.secondRoll = False
        self.previousRoll = 0
        self.die1 = Die(6)
        self.die2 = Die(6)
        self.payouts = {4:2, 5:1.5, 6:1.2, 8:1.2, 9:1.5, 10:1.2}
        self.results = "Welcome to Craps!"
        self.rollButton.clicked.connect(self.rollButtonClickedHandler)


    def __str__(self):
        return "Bank: %i Wins: %i Losses: %i " % (self.getCurrentBank(), self.getWinsCount(), self.getLossesCount())

    def setWinsCount(self, newWinsCount):
        self.winsCount = newWinsCount

    def getWinsCount(self):
        return self.winsCount

    def setLossesCount(self, newLossesCount):
        self.LossesCount = newLossesCount

    def getLossesCount(self):
        return self.lossesCount

    def getRollNumber(self):
        if self.secondRoll:
            return 2
        else:
            return 1

    def setCurrentBet(self, newCurrentBet):
        self.currentBet = newCurrentBet

    def getCurrentBet(self):
        return self.currentBet

    def setCurrentBank(self, newCurrentBank):
        self.currentBank = newCurrentBank

    def getCurrentBank(self):
        return self.currentBank

    def getCurrentRoll(self):
        return self.currentRoll

    def placeBet(self, betValue):
        self.setCurrentBet(betValue)

    def throwDice(self):
        self.currentRoll = self.die1.roll() + self.die2.roll()
        print("Roll: %i" % self.currentRoll)
        if self.secondRoll == False:
            if self.currentRoll == 7 or self.currentRoll == 11:
                print("You Win!")
                self.currentBank += self.currentBet
                self.winsCount += 1
            elif self.currentRoll == 2 or self.currentRoll == 3 or self.currentRoll == 12:
                print("You Lose")
                self.currentBank -= self.currentBet
                self.LossesCount += 1
            else:
                self.secondRoll = True
                self.previousRoll = self.currentRoll
        else:
            if self.previousRoll == self.currentRoll:
                print("You Win!")
                self.currentBank += self.currentBet * self.payouts[self.previousRoll]
            else:
                print("You Lose")
                self.currentBank -= self.currentBet * self.payouts[self.previousRoll]
                self.lossesCount +=1
