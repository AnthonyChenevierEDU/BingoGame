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
    for roll in range(dice_count):
        result = ("<p>(D{0}) Roll {1}/{2}: {3}</p>"
                  .format(str(faces), str(roll + 1), dice_count, dice.dice_roll(faces)))
        document.querySelector("div#roll-history").innerHTML += result

    document.querySelector("div#roll-history").innerHTML += "<br />"


def clear_history(event):
    document.querySelector("div#roll-history").innerHTML = ""
