from blackjackClasses import *
from commonGameFunctions import *
import random
def main():
    print("\t\tWelcome to Blackjack!\n")
    names=[]
    number = getNum_inRng("How many players? (1-7): ", low=1, high=8)
    for i in range(number):
        name = input("enter the players name")
        names.append(name)
    game = Bj_Game(names)
    again = None
    while again != "n":
        game.play()
        again = askYorN("\nDo you want to play again?: ")

main()