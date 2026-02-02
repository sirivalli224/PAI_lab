def solve_water_jug_dfs(cap1, cap2, target):
    stack = [(0, 0, [])]  # Stack stores (jug1, jug2, path)
    visited = set([(0, 0)])

    while stack:
        j1, j2, path = stack.pop()  # DFS uses pop from stack

        if j1 == target or j2 == target:
            return path + [(j1, j2)]

        # Possible moves
        moves = [
            (cap1, j2),  # Fill jug 1
            (j1, cap2),  # Fill jug 2
            (0, j2),     # Empty jug 1
            (j1, 0),     # Empty jug 2
            (min(cap1, j1 + j2), j2 - (min(cap1, j1 + j2) - j1)),  # Pour jug 2 → jug 1
            (j1 - (min(cap2, j1 + j2) - j2), min(cap2, j1 + j2))   # Pour jug 1 → jug 2
        ]

        for next_state in moves:
            if next_state not in visited:
                visited.add(next_state)
                stack.append((next_state[0], next_state[1], path + [(j1, j2)]))

    return "No Solution"


# ----------- Run -----------
cap1 = int(input("Enter capacity of jug 1: "))
cap2 = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target amount: "))

result = solve_water_jug_dfs(cap1, cap2, target)

if result == "No Solution":
    print("No solution exists.")
else:
    print("Steps to reach the target:")
    for step in result:
        print(step)
