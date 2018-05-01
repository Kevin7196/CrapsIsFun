from die import Die

die1 = Die()
die2 = Die(startingNumberOfSides = 6, startingColor = 'Blue', startingStartingValue = 1, startingIncrementValue = 10)
die3 = Die(startingNumberOfSides = 20, startingColor = 'Purple', startingStartingValue = 1, startingIncrementValue = 20)

print(die1.roll())
print(die1)
print(die2.roll())
print(die2)
print(die3.roll())
print(die3)

from die import *
import sys
import diceResources_rc
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import  QMainWindow, QWidget, QApplication

class Dice( QMainWindow) :
    """A game of Dice."""
    die1 = die2 = None

    def __init__( self, parent=None ):
        """Build a game with two dice."""

        super().__init__(parent)
        uic.loadUi("Dice.ui", self)

        self.die1 = Die()
        self.die2 = Die()

        self.rollButton.clicked.connect(self.rollButtonClickedHandler)

    def __str__( self ):
        """String representation for Dice.
        """

        return "Die1: %s\nDie2: %s" % ( self.die1, self.die2)

    def updateUI ( self ):
        self.die1View.setPixmap(QtGui.QPixmap(":/" + str(self.die1.getValue())))
        self.die2View.setPixmap(QtGui.QPixmap(":/" + str(self.die2.getValue())))
        pass

    #@QtCore.pyqtSignature("")          # Player asked for another roll of the dice.
    def rollButtonClickedHandler ( self ):
        print("Roll button clicked")
        self.die1.roll()
        self.die2.roll()
        self.updateUI()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    diceApp = Dice()
    diceApp.updateUI()
    diceApp.show()
    sys.exit(app.exec_())

