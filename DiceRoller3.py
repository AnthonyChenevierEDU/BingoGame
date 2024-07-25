"""\
This script roll sa 6-, 10- or 20- sided dice RollCount number of times.
Usage: diceRoller3.py RollCount [D6,d6,D10,d10,D20,d20]
"""
import random  # import the random library module
import sys  # import the system library

# store arguments in variables
diceType = sys.argv[1]
rollCount = int(sys.argv[2])

# set the range of values from the first command line argument
faceRange = 0

if (diceType == 'd6' or diceType == 'D6'):
    faceRange = range(1, 6)
    print("Rolling a D6 " + str(rollCount) + " times: ")
elif (diceType == 'd20' or diceType == 'D20'):
    faceRange = range(1, 20)
    print("Rolling a D20 " + str(rollCount) + " times: ")
elif (diceType == 'd10' or diceType == 'D10'):
    faceRange = range(1, 10)
    print("Rolling a D10 " + str(rollCount) + " times: ")


for i in range(rollCount):
    faceValue = random.choice(faceRange)
    print(str(i+1) + ": " + str(faceValue))

