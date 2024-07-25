"""\
This script outputs a random number between 1 and 6 inclusive (a 6-sided dice) X number of times
Usage: DiceRoller2.py RollCount
"""

import random  # import the random library module
import sys

rollCount = int(sys.argv[1])

faceRange = range(1, 6)
print("Rolling a D6 " + str(rollCount) + " times")

for i in range(rollCount):
    faceValue = random.choice(faceRange)
    print(str(i+1) + ": " + str(faceValue))
