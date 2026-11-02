import random
# Calculate number of conflicts
def calculate_cost(state):
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:
                conflicts += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts
# Generate neighboring states
def get_neighbors(state):
    n = len(state)
    neighbors = []
    for col in range(n):
        for row in range(n):
            if row != state[col]:
                new_state = state.copy()
                new_state[col] = row
                neighbors.append(new_state)
    return neighbors
# Display chessboard
def display_board(state):
    n = len(state)
    for row in range(n):
        for col in range(n):
            if state[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
# Hill Climbing algorithm
def hill_climbing(n):
    if n < 1:
        print("Invalid input!")
        return
    if n == 2 or n == 3:
        print("No solution exists!")
        return
    if n == 1:
        print("Solution found!")
        display_board([0])
        return
    restarts = 0
    steps = 0
    while restarts < 1000:
        # Random initial state
        state = [random.randrange(n) for _ in range(n)]
        while True:
            current_cost = calculate_cost(state)
            # Check goal
            if current_cost == 0:
                print("Solution found!")
                print("Final state:", state)
                print("Conflicts:", current_cost)
                print("Steps:", steps)
                print("Restarts:", restarts)
                display_board(state)
                return
            # Generate neighbors
            neighbors = get_neighbors(state)
            # Find best neighbor
            best_cost = min(
                calculate_cost(x) for x in neighbors
            )
            # Local minimum
            if best_cost >= current_cost:
                break
            best_neighbors = [
                x for x in neighbors
                if calculate_cost(x) == best_cost
            ]
            state = random.choice(best_neighbors)
            steps += 1
        restarts += 1
    print("Solution not found!")
# Main program
n = int(input("Enter number of queens: "))
hill_climbing(n)
