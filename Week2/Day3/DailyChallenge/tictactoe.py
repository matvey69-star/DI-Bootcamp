def create_board():
    """Create and return an empty 3x3 game board."""
    return [[' ' for _ in range(3)] for _ in range(3)]


def display_board(board):
    """Display the current state of the game board."""
    print("\n")
    print("  0   1   2")
    for i in range(3):
        print(f"{i} {board[i][0]} | {board[i][1]} | {board[i][2]}")
        if i < 2:
            print(" -----------")
    print("\n")


def player_input(board, player):
    """
    Get valid input from the player.
    Returns the row and column as a tuple.
    """
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))
            
            # Check if input is within valid range
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid position! Row and column must be between 0 and 2.")
                continue
            
            # Check if the cell is empty
            if board[row][col] != ' ':
                print("That position is already taken! Choose another.")
                continue
            
            return row, col
        
        except ValueError:
            print("Invalid input! Please enter numbers only.")
        except Exception as e:
            print(f"An error occurred: {e}")


def check_win(board, player):
    """
    Check if the current player has won.
    Returns True if player has won, False otherwise.
    """
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonal (top-left to bottom-right)
    if all(board[i][i] == player for i in range(3)):
        return True
    
    # Check diagonal (top-right to bottom-left)
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False


def check_tie(board):
    """
    Check if the game is a tie.
    Returns True if all positions are filled, False otherwise.
    """
    for row in board:
        if ' ' in row:
            return False
    return True


def play():
    """Main game loop that manages the game flow."""
    print("Welcome to Tic Tac Toe!")
    print("Players will take turns marking the board.")
    print("Player 1 is 'X' and Player 2 is 'O'")
    
    # Initialize the game
    board = create_board()
    players = ['X', 'O']
    current_player_idx = 0
    
    # Main game loop
    while True:
        current_player = players[current_player_idx]
        
        # Display the board
        display_board(board)
        
        # Get player input
        row, col = player_input(board, current_player)
        
        # Update the board
        board[row][col] = current_player
        
        # Check for a winner
        if check_win(board, current_player):
            display_board(board)
            print(f"🎉 Congratulations! Player {current_player} wins! 🎉")
            break
        
        # Check for a tie
        if check_tie(board):
            display_board(board)
            print("It's a tie! Good game!")
            break
        
        # Switch to the next player
        current_player_idx = 1 - current_player_idx
    
    # Ask if players want to play again
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again == 'yes' or play_again == 'y':
        play()
    else:
        print("Thanks for playing!")


# Run the game
if __name__ == "__main__":
    play()