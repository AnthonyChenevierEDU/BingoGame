"""\
This script roll sa 6-, 10- or 20- sided dice RollCount number of times.
Usage: diceRoller3.py RollCount [D6,d6,D10,d10,D20,d20]
"""
import random  # import the random library module
import sys  # import the system library


def roll_dice(faces):
    face_range = range(1, faces + 1)
    return random.choice(face_range)


# store arguments in variables
dice_type = sys.argv[2]
roll_count = int(sys.argv[1])

# set the range of values from the first command line argument
faceRange = 0

if dice_type == 'd6' or dice_type == 'D6':
    faceRange = 6
    print("Rolling a D6 " + str(roll_count) + " times: ")
elif dice_type == 'd20' or dice_type == 'D20':
    faceRange = 20
    print("Rolling a D20 " + str(roll_count) + " times: ")
elif dice_type == 'd10' or dice_type == 'D10':
    faceRange = 10
    print("Rolling a D10 " + str(roll_count) + " times: ")

for i in range(roll_count):
    faceValue = roll_dice(faceRange)
    print(str(i + 1) + ": " + str(faceValue))
