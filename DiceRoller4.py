"""\
This script rolls a 2-, 4-, 6-, 8-, 10-, 20- or 100-sided dice RollCount number of times.
Usage: diceRoller4.py RollCount [D2,d2,D4,d4,D6,d6,D8,d8,D10,d10,D20,d20, D100,d100]
"""
import sys  # import the system library
import random  # import the random library module
from Web import dice


# store both arguments in variables as integers
diceType = int(sys.argv[1])
rollCount = int(sys.argv[2][1:])

# check if diceType is not allowed, and if not then print an error message.
if diceType not in [2, 4, 6, 8, 10, 20, 100]:
    print("Invalid dice type: " + sys.argv[1] +
          "\nMust be one of D2, D4, D6, D8, D10, D20 or D100")
else:  # roll rollCount number of dice
    print("Rolling a D" + str(diceType) + " " + str(rollCount) + " times: ")
    for i in range(rollCount):
        print("Dice " + str(i + 1) + ": " + dice.dice_roll(diceType))
