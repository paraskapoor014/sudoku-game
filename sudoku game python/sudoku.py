def find_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid(board, num, pos):
    row, col = pos
    # Check row
    for i in range(9):
        if board[row][i] == num and i != col:
            return False
    # Check column
    for i in range(9):
        if board[i][col] == num and i != row:
            return False
    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve_sudoku(board):
    find = find_empty_location(board)
    if not find:
        return True
    row, col = find
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def get_user_input_board():
    board = []
    print("Enter the Sudoku puzzle row by row, use '0' for empty cells:")
    for i in range(9):
        while True:
            row_input = input(f"Enter row {i + 1} (9 digits separated by spaces): ")
            row_values = row_input.split()
            if len(row_values) != 9:
                print("Invalid input. Please enter exactly 9 digits.")
                continue
            try:
                row = [int(val) for val in row_values]
                if all(0 <= x <= 9 for x in row):
                    board.append(row)
                    break
                else:
                    print("Invalid input. Numbers should be between 0 and 9.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
    return board

if __name__ == "__main__":
    board = get_user_input_board()
    print("\nSudoku puzzle:")
    for row in board:
        print(row)
    if solve_sudoku(board):
        print("\nSolved Sudoku:")
        for row in board:
            print(row)
    else:
        print("\nNo solution exists.")
