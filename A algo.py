import heapq
GOAL = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)
goal_pos = {
    tile: (i // 3, i % 3)
    for i, tile in enumerate(GOAL)
}
# Heuristic 1: Tiles Out of Place
def misplaced(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            count += 1
    return count
# Heuristic 2: Manhattan Distance
def manhattan(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile != 0:
            r1, c1 = i // 3, i % 3
            r2, c2 = goal_pos[tile]
            distance += abs(r1-r2) + abs(c1-c2)
    return distance
# Generate neighboring states
def neighbors(state):
    result = []
    zero = state.index(0)
    r, c = zero // 3, zero % 3
    moves = [(-1, 0), (1, 0),
             (0, -1), (0, 1)]
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_zero = nr * 3 + nc
            temp = list(state)
            temp[zero], temp[new_zero] = (
                temp[new_zero], temp[zero]
            )
            result.append(tuple(temp))
    return result
# Check solvability
def is_solvable(state):
    a = [x for x in state if x != 0]
    b = [x for x in GOAL if x != 0]
    inv_a = sum(
        a[i] > a[j]
        for i in range(8)
        for j in range(i+1, 8)
    )
    inv_b = sum(
        b[i] > b[j]
        for i in range(8)
        for j in range(i+1, 8)
    )
    return inv_a % 2 == inv_b % 2
# A* Search
def astar(start, heuristic):
    if not is_solvable(start):
        print("No solution exists!")
        return
    pq = []
    heapq.heappush(
        pq, (heuristic(start), 0, start)
    )
    parent = {start: None}
    cost = {start: 0}
    while pq:
        f, g, current = heapq.heappop(pq)
        if g != cost[current]:
            continue
        if current == GOAL:
            path = []
            node = current
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            print("\nSolution Path:")
            for state in path:
                for i in range(0, 9, 3):
                    print(state[i:i+3])
                print()
            print("Number of moves:", len(path)-1)
            return
        for nxt in neighbors(current):
            new_g = g + 1
            if new_g < cost.get(nxt, float('inf')):
                cost[nxt] = new_g
                parent[nxt] = current
                h = heuristic(nxt)
                new_f = new_g + h
                heapq.heappush(
                    pq, (new_f, new_g, nxt)
                )
    print("No solution found!")
# Main program
print("1. Tiles Out of Place")
print("2. Manhattan Distance")
choice = int(input("Enter heuristic choice: "))
print("Enter 9 numbers separated by spaces:")
start = tuple(map(int, input().split()))
if len(start) != 9 or sorted(start) != list(range(9)):
    print("Invalid puzzle!")
else:
    if choice == 1:
        astar(start, misplaced)
    elif choice == 2:
        astar(start, manhattan)
    else:
        print("Invalid choice!")
