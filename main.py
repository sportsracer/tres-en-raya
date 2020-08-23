# Create an empty board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def computer_plays():
    """
    Let the computer play. It will place an "X" on the board.
    """
    # Right now, the computer just places its "X" in the first empty field. Needs to be optimized!
    for row in [0, 1, 2]:
        for column in [0, 1, 2]:
            if board[row][column] == " ":
                board[row][column] = "X"
                return


def human_plays():
    """
    Let the human play. Ask her or him for the row and column to place the "O".
    """
    column = int(input("Which column? (0, 1 or 2) "))
    row = int(input("Which row? (0, 1 or 2) "))
    board[row][column] = "O"


def is_game_over():
    """
    Returns `False` if the game is not over yet. Or it returns "Tie" if there's a tie, or "X"/"O" if a player has won.
    """
    for player in ["O", "X"]:

        # First, check if any of the rows have the same symbol three time
        for row in [0, 1, 2]:
            if all(board[row][column] == player for column in [0, 1, 2]):
                return player

        # Then, do the same check for columns
        for column in [0, 1, 2]:
            if all(board[row][column] == player for row in [0, 1, 2]):
                return player

        # Check the first diagonal
        if all(board[row][column] == player for row, column in [(0, 0), (1, 1), (2, 2)]):
            return player

        # Check the second diagonal
        if all(board[row][column] == player for row, column in [(2, 0), (1, 1), (0, 2)]):
            return player

    # No player has won … let's check if it's a tie
    for row in [0, 1, 2]:
        for column in [0, 1, 2]:
            if board[row][column] == " ":
                # There's still at least one empty spot … keep playing!
                return False

    # No player has won, and there are no empty fields left … we are sure it's a tie!
    return "Tie"


def print_board():
    """
    Print the current state of the board to the console.
    """
    print("┼───┼───┼───┼")
    for row in board:
        print(f"│ {row[0]} │ {row[1]} │ {row[2]} │")
        print("┼───┼───┼───┼")


while True:
    # Let both players make their move, and after each move, check if there's a winner or a tie

    print_board()

    human_plays()
    winner = is_game_over()
    if winner:
        print(f"{winner} takes it all!")
        break

    computer_plays()
    winner = is_game_over()
    if winner:
        print(f"{winner} takes it all!")
        break

# Game is over! Show the final state of the board:
print_board()
