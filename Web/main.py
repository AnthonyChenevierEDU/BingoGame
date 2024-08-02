import random  # import the random library module
from pyscript import document
import dice


# GLOBAL (program-wide) variable
# this list holds the selections and
# counts made for each dice type
# each entry in the list is a tuple
# containing number of dice to roll for that type
# key = dice type
# val - dice count
# i.e. dice_selection[0] = ( "D6", 20 )
dice_selection = []

def add_dice(type_count):
    elem = document.querySelector("div#dice-" + type_count)
    elem.


def select_option(event=None):
    if event:
        t_id = event.target.id
        print(t_id)

        #selected_faces[t_id] = event.target.value
        #print("Changed faces to " + selected_faces[t_id])


def roll(event):
    global selected_faces
    dc = int(document.querySelector("input#dice-count-" + selected_faces).value)
    rolls = []
    faces = 0
    for i in range(dc):
        if selected_faces == "Coin":
            faces = 2
        else:
            faces = selected_faces[1:]
        rolls.append("(D" + faces + ") Roll " + str(i+1) + ": " + dice.dice_roll(faces) + "<br/>")

    output = document.querySelector("p#output")
    output.innerHTML = rolls
