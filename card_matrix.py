board_matrix = [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]


def reset_card():
    global board_matrix
    board_matrix = [[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]


def set_position(x, y):
    global board_matrix
    board_matrix[x-1][y-1] = 1
    if check_card():
        return True
    return False


def get_position(x, y):
    return board_matrix[x-1][y-1]


def check_card():
    global board_matrix
    # Check rows
    for row in board_matrix:
        if all(cell == 1 for cell in row):
            return True

    # Check columns
    for col in range(5):
        if all(row[col] == 1 for row in board_matrix):
            return True

    # Check top-left to bottom-right diagonal
    if all(board_matrix[i][i] == 1 for i in range(5)):
        return True

    # Check top-right to bottom-left diagonal
    if all(board_matrix[i][4 - i] == 1 for i in range(5)):
        return True

    return False
