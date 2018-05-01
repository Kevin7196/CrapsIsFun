from die import Die
import sys
import crapsResources_rc
from time import sleep
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class CrapsGame(QMainWindow):
    """A Game of Craps."""

    def __init__( self, parent=None):
        """Build a game with two dice."""

        super().__init__(parent)
        uic.loadUi("crapsUI.ui", self)
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
        self.payouts = {4: 2, 5: 1.5, 6: 1.2, 8: 1.2, 9: 1.5, 10: 1.2}
        self.results = "Welcome to Craps!"
        self.rollButton.clicked.connect(self.betSystem)

    def betSystem(self):
        try:
            betAmt = int(self.bankBet.toPlainText())
            self.placeBet(betAmt)
            self.rollButtonClickedHandler()
        except:
            self.results = "You cannot bet in letters or just integers."
        self.updateUI()

    def __str__(self):
        """String representation for Dice."""
        return""

    def updateUI (self):
        if self.getCurrentBank() <= 0:
            self.results = " You lost all your money."
            self.rollButton.setEnabled(False)
        self.winsLabel.setText(str(self.winsCount))
        self.lossesLabel.setText(str(self.lossesCount))
        self.resultsLabel.setText(str(self.results))
        self.die1View.setPixmap(QtGui.QPixmap(":/" + str(self.die1.getValue())))
        self.die2View.setPixmap(QtGui.QPixmap(":/" + str(self.die2.getValue())))
        self.bankAmt.setText(str(self.getCurrentBank()))


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

    @pyqtSlot()         #Player asked for a roll of dice.
    def rollButtonClickedHandler(self):
        print ("Roll button clicked!")
        self.currentRoll = self.die1.roll() + self.die2.roll()
        if self.secondRoll:
            print("Roll: %i Second" % self.currentRoll)
        else:
            print("Roll: %i First" % self.currentRoll)
        if self.secondRoll == False:
            if self.currentRoll == 7 or self.currentRoll == 11:
                self.results = ("You Win!")
                self.currentBank += self.currentBet
                self.winsCount += 1
            elif self.currentRoll == 2 or self.currentRoll == 3 or self.currentRoll == 12:
                self.results = ("You Lose")
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
                self.results = ("You Lose")
                self.currentBank -= self.currentBet * self.payouts[self.previousRoll]
                self.lossesCount += 1
            self.secondRoll = False
        self.updateUI()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    crapsApp = CrapsGame()
    crapsApp.updateUI()
    crapsApp.show()
    sys.exit(app.exec_())


