board = [" " for _ in range(9)] 
def print_board(): # prints the board
    print(f"""
     {board[0]} | {board[1]} | {board[2]}
    ---+---+---
     {board[3]} | {board[4]} | {board[5]}
    ---+---+---
     {board[6]} | {board[7]} | {board[8]}
    """)

def check_winner(): # checks possible winning combos
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for combo in win_combinations: #checks for winners
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return True  
    return False


def is_squares_full():
    return " " not in board


def play_game():
    print("Welcome to Tic-Tac-Toe by Himeli!")
    print("Player 1 is X and Player 2 is O. Let's get started!")
    current_player = "X" 

    while True:
        print_board()
        print(f"Your turn, Player {current_player}!")
        try:
            move = int(input("Pick a number between 0 and 8 to place your mark: "))
            if move < 0 or move > 8 or board[move] != " ":
                print("That’s not a valid move. Try again!")
                continue
            board[move] = current_player
            if check_winner():
                print_board()
                print(f"Player {current_player} wins! Nice job!")
                break
            if is_squares_full():
                print_board()
                print("It’s a tie! Great game, everyone!")
                break
            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Oops! Please enter a number between 0 and 8.")


if __name__ == "__main__":
    play_game()
