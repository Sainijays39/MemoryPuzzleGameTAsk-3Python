import random
import time

# Constants
BOARD_SIZE = 4  # 4x4 board
NUM_PAIRS = (BOARD_SIZE * BOARD_SIZE) // 2
TIME_LIMIT = 60  # Time limit in seconds

def create_board():
    """Create a shuffled board with pairs of cards."""
    cards = list(range(NUM_PAIRS)) * 2
    random.shuffle(cards)
    board = [cards[i:i + BOARD_SIZE] for i in range(0, len(cards), BOARD_SIZE)]
    return board

def display_board(board, revealed):
    """Display the game board with revealed cards."""
    print("\nBoard:")
    for row in range(BOARD_SIZE):
        row_display = ""
        for col in range(BOARD_SIZE):
            if (row, col) in revealed:
                row_display += f" {board[row][col]} "
            else:
                row_display += " * "
        print(row_display)

def get_user_input():
    """Get user input for selecting two cards."""
    while True:
        try:
            r1, c1 = map(int, input("Enter the row and column for the first card (e.g., 1 2): ").split())
            r2, c2 = map(int, input("Enter the row and column for the second card (e.g., 3 4): ").split())
            if (0 <= r1 < BOARD_SIZE and 0 <= c1 < BOARD_SIZE and
                0 <= r2 < BOARD_SIZE and 0 <= c2 < BOARD_SIZE and
                (r1 != r2 or c1 != c2)):
                return (r1, c1), (r2, c2)
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")

def main():
    board = create_board()
    revealed = set()
    matched = set()
    start_time = time.time()
    
    while len(matched) < NUM_PAIRS:
        elapsed_time = time.time() - start_time
        if elapsed_time > TIME_LIMIT:
            print("Time's up!")
            break
        
        display_board(board, revealed)
        print(f"Time left: {int(TIME_LIMIT - elapsed_time)} seconds")
        
        card1, card2 = get_user_input()
        
        if card1 in revealed or card2 in revealed:
            print("Card already revealed. Choose different cards.")
            continue
        
        revealed.add(card1)
        revealed.add(card2)
        
        r1, c1 = card1
        r2, c2 = card2
        
        if board[r1][c1] == board[r2][c2]:
            print("It's a match!")
            matched.add(board[r1][c1])
            revealed = {x for x in revealed if board[x[0]][x[1]] in matched}
        else:
            print("Not a match. Try again.")
            time.sleep(1)  # Pause before hiding cards again
            revealed.discard(card1)
            revealed.discard(card2)
    
    if len(matched) == NUM_PAIRS:
        print("Congratulations! You've matched all pairs!")
    else:
        print("Game Over. Better luck next time!")

if __name__ == "__main__":
    main()
