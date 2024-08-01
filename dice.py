import random  # import the random library module


# Function: dice_roll
# Params: int(faces)
# Returns: string with result of dice roll
def dice_roll(faces):
    face_range = range(1, faces+1)
    face_value = random.choice(face_range)
    return "Rolled a " + str(face_value)
