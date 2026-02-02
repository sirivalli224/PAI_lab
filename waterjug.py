from collections import deque

def solve_water_jug(cap1, cap2, target):
    queue = deque([(0, 0, [])])
    visited = set([(0, 0)])

    while queue:
        j1, j2, path = queue.popleft()

        if j1 == target:
            return path + [(j1, j2)]

        moves = [
            (cap1, j2),  
            (j1, cap2),  
            (0, j2),     
            (j1, 0),     
            (
                min(cap1, j1 + j2),
                j2 - (min(cap1, j1 + j2) - j1)
            ),
            (
                j1 - (min(cap2, j1 + j2) - j2),
                min(cap2, j1 + j2)
            )
        ]

        for next_state in moves:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state[0], next_state[1], path + [(j1, j2)]))

    return "No Solution"

cap1 = int(input("Enter capacity of jug 1: "))
cap2 = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target amount: "))

result = solve_water_jug(cap1, cap2, target)

if result == "No Solution":
    print("No solution exists.")
else:
    print("Steps to reach the target:")
    for step in result:
        print(step)
