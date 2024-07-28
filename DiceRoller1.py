"""\
This script outputs a random number between 1 and 6 inclusive - i.e. a 6-sided dice.
Usage: DiceRoller1.py
"""
import random  # import the random module

# set the range of values
diceRange = range(1, 6)
print(diceRange)
faceValue = random.choice(diceRange)

print(faceValue)
