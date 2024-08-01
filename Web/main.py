import random  # import the random library module
from pyweb import pydom


# Function: dice_roll
# Params: int(faces)
# Returns: string with result of dice roll
def dice_roll(faces):
    face_range = range(1, faces)
    face_value = random.choice(face_range)
    return "Rolled a " + str(face_value)

selected_faces = "Coin"
def change_handler(event = None):
    global selected_faces
    if event:
        selected_faces = event.target.value
        print("BA" . selected_faces)

def roll(event):
    dc = pydom["input#dice-count"][0].value
    print(dc)
    print(selected_faces)
    for _ in range(dc):
        if faces == "Coin":
            faces = "D2"

    current_roll = dice_roll(int(faces[1:]))
    pydom["p#output"].content = current_roll
