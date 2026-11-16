import random
import math
def display_board(board):
    """Display the chessboard."""
    n = len(board)
    for r in range(n):
        print(" ".join("Q" if board[c] == r else "." for c in range(n)))
    print()
def compute_attacks(board):
    """Calculate the number of attacking queen pairs."""
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts
def random_move(board):
    """Move one queen to another row in the same column."""
    n = len(board)
    new_board = board.copy()
    col = random.randrange(n)
    new_row = random.randrange(n)
    new_board[col] = new_row
    return new_board
def simulated_annealing(n, start_temp=120, alpha=0.95, stop_temp=0.1):
    current = [random.randrange(n) for _ in range(n)]
    curr_cost = compute_attacks(current)
    best = current.copy()
    best_cost = curr_cost
    temperature = start_temp
    step = 1
    print("Initial Board:")
    display_board(current)
    print("Initial Conflicts:", curr_cost)
    while temperature > stop_temp and curr_cost != 0:
        nxt = random_move(current)
        nxt_cost = compute_attacks(nxt)
        delta = nxt_cost - curr_cost
        if delta <= 0:
            current = nxt
            curr_cost = nxt_cost
        else:
            p = math.exp(-delta / temperature)
            if random.random() < p:
                current = nxt
                curr_cost = nxt_cost
        if curr_cost < best_cost:
            best = current.copy()
            best_cost = curr_cost
        if step % 10 == 0 or curr_cost == 0:
            print("Step", step, "| Temp:", round(temperature, 2),
                  "| Conflicts:", curr_cost)
        temperature = alpha * temperature
        step += 1
    print("\nFinal Board Configuration:")
    display_board(best)
    print("Final Conflicts:", best_cost)
    if best_cost == 0:
        print("Solution Found!")
    else:
        print("Best State Found.")
random.seed(45)
simulated_annealing(8)
