# a list for the game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
# states the game is on going. Will break later on
game_on_going = True

winner = None
# first move
current_player = "X"


# function that prints out the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# function beginning the game
def play():
    # calls the function for printing the board
    display_board()
    # loop with functions that assigns the turn to either X or O, check if the game is won or tied, and changes
    # players via turns
    while game_on_going:
        turn(current_player)

        game_status()

        change_player()
    # prints the letter of the winner based on the functions below
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie")


# the player turn function that is called on 27, input position of board
def turn(player):
    print(player + "'s turn")
    position = input('Pick a spot between 1-9: ')
    # if player inputs anything other than numbers 1-9 then this will loop requesting a valid input
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input('Invalid choice, please try again: ')
        # indexes start at 0, so -1 equals the index the player chooses.
        position = int(position) - 1
        # ensures players cannot overwrite a position 1-9 that is already taken
        if board[position] == "-":
            valid = True
        else:
            print('You cannot go there, try again')

    board[position] = player

    display_board()


# game_status function is called on line 29. This determines a win or tie, with 2 function calls being defined below
def game_status():
    check_win()
    check_tie()


# called under game_status function. 3 function calls for the 3 ways too win: across, diagonal, up and down.
def check_win():
    global winner
    row_winner = check_rows()

    column_winner = check_columns()
    # returns the letter in any of those indexes for victory
    diag_winner = check_diag()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner = None
    return


def check_rows():
    global game_on_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_on_going = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return

# checks the columns for victory
def check_columns():
    global game_on_going
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    # returns the letter in any of those indexes for victory
    if col_1 or col_2 or col_3:
        game_on_going = False
    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]
    return


# function checks diagonal victory
def check_diag():
    global game_on_going
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    # returns the letter in any of those indexes for victory
    if diag_1 or diag_2:
        game_on_going = False
    if diag_1:
        return board[0]
    if diag_2:
        return board[2]
    return


# checking for tie
def check_tie():
    global game_on_going
    if "-" not in board:
        game_on_going = False
    return


def change_player():
    # Global variables we need
    global current_player
    # If the current player was X, make it O
    # setting a value is = aka assignment operator
    # == is for comparison of two variables, checking if they are equal
    if current_player == "X":
        current_player = "O"
    # Or if the current player was O, make it X
    elif current_player == "O":
        current_player = "X"
        return

# calls the play function to kick off the program!
play()
