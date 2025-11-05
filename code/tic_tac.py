# Initialize the board
board = [" " for _ in range(9)]

# Function to display the board
def print_board():
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Function to check for a win
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to check for a draw
def check_draw():
    return " " not in board

# Main game loop
def play_game():
    current_player = "X"
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = current_player
                print_board()

                if check_win(current_player):
                    print(f"🎉 Player {current_player} wins!")
                    break
                elif check_draw():
                    print("It's a draw!")
                    break

                current_player = "O" if current_player == "X" else "X"
            else:
                print("That spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

# Run the game
play_game()
