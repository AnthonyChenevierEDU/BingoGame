"""\
This script outputs a random number between 1 and 6 inclusive (a 6-sided dice) X number of times
Usage: DiceRoller2.py RollCount
"""

import random  # import the random library module
import sys


def roll_dice():
    face_range = range(1, 7)
    return random.choice(face_range)


roll_count = int(sys.argv[1])
print("Rolling a D6 " + str(roll_count) + " times")

for i in range(roll_count):
    print(str(i + 1) + ": " + str(roll_dice()))
