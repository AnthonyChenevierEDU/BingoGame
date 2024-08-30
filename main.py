import random
from pyscript import document
import card_matrix

caller_numbers = []
card_numbers = []


def shuffle_caller():
    global caller_numbers
    print("Calling 'shuffle_caller'")
    caller_numbers = list(range(1,76))
    random.shuffle(caller_numbers)
    for i in range(75):
        document.querySelector(f"#cell_{i+1}").style.fontWeight = 'normal'


def generate_card():
    print("Calling 'generate_card'")
    global card_numbers
    card_numbers = list(range(1,76))
    random.shuffle(card_numbers)
    card_numbers = card_numbers[:25]

    for x in range(5):
        for y in range(5):
            bid = f"#bcell_{x+1}_{y+1}"
            document.querySelector(bid).innerHTML = card_numbers.pop()


def call_next(event):
    global caller_numbers
    print("calling 'call_next'")
    if len(caller_numbers) > 0:
        next_num = caller_numbers.pop()
        document.querySelector(f"#cell_{next_num}").style.fontWeight = 'bold'


def reset_game(event):
    print("calling 'reset_game'")
    shuffle_caller()
    generate_card()


def check_cell(event):
    print("calling 'check_cell'")
    cell_id = event.target.id
    print(cell_id)


#initial setup
reset_game(0)
