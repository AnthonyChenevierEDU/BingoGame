from pyscript import document
import dice


# GLOBAL (script-wide) variable
# this stores the selected face option from the drop-down list
dice_type = "Coin"


def select_face_option(event):
    global dice_type  # use global dice_type
    dice_type = event.target.value
    # print a debugging statement to the console
    print("Changed dice_type to " + dice_type)


def roll_all_dice(event):
    global dice_type
    if dice_type == "Coin":
        faces = 2
    else:
        faces = int(dice_type[1:])

    for roll in range(int(document.querySelector("input#dice-count").value)):
        result = f"<p>(D{str(faces)}) Roll {str(roll + 1)}: {dice.dice_roll(faces)}</p>"
        document.querySelector("div#roll-history").innerHTML += result

    document.querySelector("div#roll-history").innerHTML += "<br />"


def clear_history(event):
    document.querySelector("div#roll-history").innerHTML = ""
