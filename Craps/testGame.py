__author__ = 'Lisbeth Alvarez'

from craps import CrapsGame

aCrapsGame = CrapsGame()
print(aCrapsGame.getCurrentBank())
aCrapsGame.placeBet(50)
aCrapsGame.throwDice()
aCrapsGame.throwDice()
print(aCrapsGame.getCurrentBank())