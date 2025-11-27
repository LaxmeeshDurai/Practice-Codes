def print_board(board, n):
    for i in range(n):
        row = ""
        for j in range(n):
            if board[i] == j:
                row += "Q "
            else:
                row += ". "
        print(row)
    print("\n")


def is_safe(board, row, col):
    # Check for same column and diagonals
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(board, row, n):
    if row == n:
        print_board(board, n)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            # backtrack (no explicit undo needed since we overwrite board[row])


def nqueens(n):
    board = [-1] * n
    solve_nqueens(board, 0, n)


# Run
n = int(input("Enter the value of N: "))
nqueens(n)
