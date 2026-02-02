def solve_water_jug_memo(cap1, cap2, target):
    visited = set()  # memoization to store visited states

    def dfs(j1, j2):
        # Check if we reached the target
        if j1 == target or j2 == target:
            return [(j1, j2)]
        
        # Skip already visited states
        if (j1, j2) in visited:
            return None
        visited.add((j1, j2))

        # All possible moves
        moves = [
            (cap1, j2),  # Fill jug 1
            (j1, cap2),  # Fill jug 2
            (0, j2),     # Empty jug 1
            (j1, 0),     # Empty jug 2
            (min(cap1, j1 + j2), j2 - (min(cap1, j1 + j2) - j1)),  # Pour jug2 → jug1
            (j1 - (min(cap2, j1 + j2) - j2), min(cap2, j1 + j2))   # Pour jug1 → jug2
        ]

        for nj1, nj2 in moves:
            result = dfs(nj1, nj2)
            if result:
                return [(j1, j2)] + result  # prepend current state to path

        return None  # No solution from this path

    solution = dfs(0, 0)
    return solution if solution else "No Solution"


# ---------------- Run ----------------
cap1 = int(input("Enter capacity of jug 1: "))
cap2 = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target amount: "))

result = solve_water_jug_memo(cap1, cap2, target)

if result == "No Solution":
    print(result)
else:
    print("Steps to reach the target:")
    for step in result:
        print(step)
