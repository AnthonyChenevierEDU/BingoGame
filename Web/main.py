import random  # import the random library module
from pyscript import document


# Function: dice_roll
# Params: int(faces)
# Returns: string with result of dice roll
def dice_roll(faces):
    face_range = range(1, faces+1)
    face_value = random.choice(face_range)
    return "Rolled a " + str(face_value)


selected_faces = "Coin"


def change_handler(event=None):
    global selected_faces
    if event:
        selected_faces = event.target.value
        print("Changed faces to " + selected_faces)


def roll(event):
    global selected_faces
    dc = int(document.querySelector("input#dice-count").value)
    rolls = ""
    for i in range(dc):
        if selected_faces == "Coin":
            selected_faces = "D2"
        faces = int(selected_faces[1:])
        rolls += "Roll " + str(i+1) + ": " + dice_roll(faces) + "<br/>"

    output = document.querySelector("p#output")
    output.innerHTML = rolls
