import random  # import the random library module
from pyweb import pydom


# Function: dice_roll
# Params: int(faces)
# Returns: string with result of dice roll
def dice_roll(faces):
    face_range = range(1, faces)
    face_value = random.choice(face_range)
    return "Rolled a " + str(face_value)


def roll(event):
    dc = pydom["input#dice-count"].value
    # faces = pydom["select#dice-faces"].value
    print(dc)
    # print(faces)
    #for i in range(dc):
     #   if faces == "Coin":
      #      faces = "D2"
#
 #       current_roll = dice_roll(int(faces[1:]))
  #      pydom["p#output"].content = current_roll
