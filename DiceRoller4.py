"""\
This script rolls a 2-, 4-, 6-, 8-, 10-, 20- or 100-sided dice RollCount number of times.
Usage: diceRoller4.py RollCount [D2,d2,D4,d4,D6,d6,D8,d8,D10,d10,D20,d20, D100,d100]
"""
import random  # import the random library module
import sys  # import the system library


def dice_roll(faces, rolls):
    face_range = range(1, faces)
    print("Rolling a D" + str(faces) + " " + str(rollCount) + " times: ")
    for i in range(rolls):
        face_value = random.choice(face_range)
        print(str(i + 1) + ": " + str(face_value))


# store arguments in variables
diceType = int(sys.argv[1][1:])
rollCount = int(sys.argv[2])

if (diceType in [2, 4, 6, 8, 10, 20, 100]):
    dice_roll(diceType, rollCount)
