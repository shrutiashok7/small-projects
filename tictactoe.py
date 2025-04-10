import random

def print_board(board):
    print("  1 2 3")
    for i in range(3):
        print(f"{i+1} {board[i][0]}|{board[i][1]}|{board[i][2]}")
        if i < 2:
            print("  -+-+-")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
            
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
            
    if all(board[i][i] == player for i in range(3)):
        return True
        
    if all(board[i][2-i] == player for i in range(3)):
        return True
        
    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def computer_move(board):
    empty_cells = get_empty_cells(board)
    
    for row, col in empty_cells:
        board[row][col] = "O"
        if check_winner(board, "O"):
            return row, col
        board[row][col] = " "  # Undo the move
    
    for row, col in empty_cells:
        board[row][col] = "X"
        if check_winner(board, "X"):
            board[row][col] = "O"
            return row, col
        board[row][col] = " "  # Undo the move
    
    if board[1][1] == " ":
        return 1, 1
    
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    available_corners = [corner for corner in corners if board[corner[0]][corner[1]] == " "]
    if available_corners:
        return random.choice(available_corners)

    return random.choice(empty_cells)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    print("hi, lets play tic tac toe!")
    print("You are X and go first. Enter your move as row,column (both 1-3)")
    print("For example, the top-left corner is 1,1")
    
    while True:
        print_board(board)
        
        while True:
            try:
                move = input("your move (row,column): ")
                row, col = map(int, move.split(","))

                row -= 1
                col -= 1
                
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("please enter numbers between 1 and 3.")
                    continue
                    
                if board[row][col] != " ":
                    print("that spot is already taken, try again.")
                    continue
                    
                break
            except ValueError:
                print("please enter your move as row,column (e.g., 1,1)")
        
        board[row][col] = "X"
        
        if check_winner(board, "X"):
            print_board(board)
            print("you win! congratulations!")
            break
            
        if is_board_full(board):
            print_board(board)
            print("it's a draw!")
            break
            
        print("i'm thinking...")
        comp_row, comp_col = computer_move(board)
        board[comp_row][comp_col] = "O"
        
        print(f"i chose: {comp_row+1},{comp_col+1}")
        
        if check_winner(board, "O"):
            print_board(board)
            print("i win lol! better luck next time heh")
            break
            
        if is_board_full(board):
            print_board(board)
            print("it's a draw!")
            break

if __name__ == "__main__":
    main()