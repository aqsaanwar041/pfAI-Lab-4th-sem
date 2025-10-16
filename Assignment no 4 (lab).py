

def print_board(board):
    """Display the chessboard configuration."""
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += " Q "
            else:
                line += " - "
        print(line)
    print("\n")

def is_safe(board, row, col):
    """Check if a queen can be placed at board[row] = col."""
    for r in range(row):
        
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True

def solve_n_queens(n, row=0, board=None, solutions=None):
    """Dynamic/recursive backtracking to find all solutions."""
    if board is None:
        board = [-1] * n
    if solutions is None:
        solutions = []

    if row == n:
        
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(n, row + 1, board, solutions)
            board[row] = -1  

    return solutions


if __name__ == "__main__":
    N = int(input("Enter number of queens (N): "))
    all_solutions = solve_n_queens(N)

    print(f"\nTotal Solutions for {N}-Queens: {len(all_solutions)}\n")
    for i, sol in enumerate(all_solutions, 1):
        print(f"Solution {i}:")
        print_board(sol)
