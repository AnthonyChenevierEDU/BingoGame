from pyscript import document
import dice


# GLOBAL (script-wide) variable
# this stores the selected face option from the drop-down list
dice_type = "Coin"


def select_face_option(event):
    global dice_type  # use global var named dice_type

    dice_type = event.target.value
    # print a debugging statement to the console
    print("Changed dice_type to " + dice_type)


def roll_all_dice(event):
    global dice_type  # use global var named dice_type
    # extract the number of faces to use for the dice_roll function
    if dice_type == "Coin":
        faces = 2
    else:
        faces = int(dice_type[1:])

    dice_count = int(document.querySelector("input#dice-count").value)
    roll_history_div = document.querySelector("div#roll-history")

    for dice_num in range(1, dice_count + 1):
        current_roll = dice.dice_roll(faces)
        roll_history_div.innerHTML += f"<p>(D{faces}) Roll {dice_num}/{dice_count}: {current_roll}</p>"

    roll_history_div.innerHTML += "<br />"
    roll_history_div.scrollTop = roll_history_div.scrollHeight


def clear_history(event):
    document.querySelector("div#roll-history").innerHTML = ""
