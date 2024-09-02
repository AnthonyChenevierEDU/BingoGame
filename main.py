import random
from pyscript import document
import card_matrix

all_bingo_numbers = []
called_numbers = []

card_numbers = []


def highlight_card_cell(cell_id):
    document.querySelector(cell_id).className += "highlight-card"


def reset_card_cell(cell_id):
    document.querySelector(cell_id).className = ""


def highlight_caller_cell(cell_id):
    document.querySelector(cell_id).className += "highlight-caller"


def reset_caller_cell(cell_id):
    document.querySelector(cell_id).className = ""


def reset_game(event):
    print("calling 'reset_game'")
    shuffle_caller()
    reset_calls()
    generate_card()
    document.querySelector("#win_game").close()


def shuffle_caller():
    global all_bingo_numbers
    print("Calling 'shuffle_caller'")
    
    # reshuffle the call order
    all_bingo_numbers = list(range(1, 76))
    random.shuffle(all_bingo_numbers)
 
 
def reset_calls():   
    global called_numbers
    # reset the called numbers
    called_numbers = []
    document.querySelector("#called_numbers").innerHTML = ""
    document.querySelector("#current_call").innerHTML = ""
    
    for i in range(75):
        reset_caller_cell(f"#cell_{i+1}")


def generate_card():
    global card_numbers
    print("Calling 'generate_card'")
    card_matrix.reset_card()
    card_numbers = list(range(1, 76))
    random.shuffle(card_numbers)
    card_numbers = card_numbers[:25]

    for x in range(5):
        for y in range(5):
            bid = f"#card_{x + 1}_{y + 1}"
            elem = document.querySelector(bid)
            elem.innerHTML = card_numbers.pop()
            reset_card_cell(bid)


def add_call(num):
    global called_numbers
    called_numbers.append(num)
    document.querySelector(f"#called_numbers").innerHTML = ", ".join(str(x) for x in called_numbers)
    document.querySelector("#current_call").innerHTML = str(num)


def call_next(event):
    global all_bingo_numbers
    print("calling 'call_next'")
    if len(all_bingo_numbers) > 0:
        # get the next number in our caller's shuffled list
        current_call = all_bingo_numbers.pop()
        # highlight and add the number to the call list
        add_call(current_call)
        highlight_caller_cell(f"#cell_{current_call}")



def check_cell(event):
    print("calling 'check_cell'")
    cell_id = event.target.id
    cell_val = int(event.target.innerHTML)

    coords = cell_id.split("_")[1:]
    x = int(coords[0])
    y = int(coords[1])
    if cell_val in called_numbers and card_matrix.get_position(x, y) == 0:
        highlight_card_cell(f"#{cell_id}")
        if card_matrix.set_position(x, y):
            document.querySelector("#win_game").showModal()


# initial setup
reset_game(0)
