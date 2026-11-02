# 8 Puzzle using DFS and IDDFS
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)
# Check whether puzzle is solvable
def is_solvable(state):
    numbers = [x for x in state if x != 0]
    inversions = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                inversions += 1
    return inversions % 2 == 0
# DFS
def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        state, path = stack.pop()
        if state in visited:
            continue
        visited.add(state)
        if state == goal:
            return path
        zero = state.index(0)
        row = zero // 3
        col = zero % 3
        # U, D, L, R
        moves = []
        if row > 0:
            moves.append(zero - 3)
        if row < 2:
            moves.append(zero + 3)
        if col > 0:
            moves.append(zero - 1)
        if col < 2:
            moves.append(zero + 1)
        for new_pos in moves:
            new_state = list(state)
            new_state[zero], new_state[new_pos] = \
                new_state[new_pos], new_state[zero]
            new_state = tuple(new_state)
            if new_state not in visited:
                stack.append((new_state, path + [new_state]))
    return None
# Depth Limited DFS for IDDFS
def depth_limited_dfs(state, goal, depth, path, visited):
    if state == goal:
        return path
    if depth == 0:
        return None
    zero = state.index(0)
    row = zero // 3
    col = zero % 3
    # U, D, L, R
    moves = []
    if row > 0:
        moves.append(zero - 3)
    if row < 2:
        moves.append(zero + 3)
    if col > 0:
        moves.append(zero - 1)
    if col < 2:
        moves.append(zero + 1)
    for new_pos in moves:
        new_state = list(state)
        new_state[zero], new_state[new_pos] = \
            new_state[new_pos], new_state[zero]
        new_state = tuple(new_state)
        if new_state not in visited:
            visited.add(new_state)
            result = depth_limited_dfs(
                new_state,
                goal,
                depth - 1,
                path + [new_state],
                visited
            )
            if result is not None:
                return result
            visited.remove(new_state)
    return None
# IDDFS
def iddfs(start, goal):
    depth = 0
    while True:
        visited = {start}
        result = depth_limited_dfs(
            start,
            goal,
            depth,
            [start],
            visited
        )
        if result is not None:
            return result
        depth += 1
# Print puzzle
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
# Run a test case
def run_test_case(number, start):
    print("\nTC", number)
    print("Initial state:")
    print_state(start)
    # DFS
    print("\nRunning DFS...")
    if not is_solvable(start):
        print("No solution found!")
    else:
        dfs_solution = dfs(start, GOAL)
        if dfs_solution:
            print("Solution found! Total moves:",
                  len(dfs_solution) - 1)
        else:
            print("No solution found!")
    # IDDFS
    print("\nRunning IDDFS...")
    if not is_solvable(start):
        print("No solution found!")
    else:
        iddfs_solution = iddfs(start, GOAL)
        if iddfs_solution:
            print("Solution found! Total moves:",
                  len(iddfs_solution) - 1)
            print("Step-by-step path sequence:")
            for i, state in enumerate(iddfs_solution):
                print("Step", i, ":")
                print_state(state)
        else:
            print("No solution found!")
# Test Cases
TC1 = (1, 2, 3,
       4, 5, 6,
       7, 8, 0)
TC2 = (1, 2, 3,
       4, 5, 6,
       7, 0, 8)
TC3 = (1, 2, 3,
       4, 0, 6,
       7, 5, 8)
TC4 = (1, 2, 3,
       4, 5, 6,
       8, 7, 0)
TC5 = (1, 2, 3,
       5, 0, 6,
       4, 7, 8)
# Run all test cases
run_test_case(1, TC1)
run_test_case(2, TC2)
run_test_case(3, TC3)
run_test_case(4, TC4)
run_test_case(5, TC5)

