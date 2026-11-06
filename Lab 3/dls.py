graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

def dls(node, limit):
    visited = []
    stack = []
    found = False
    stack.append((node, 0))
    while stack:
        print(stack, visited)
        temp, depth = stack.pop()
        visited.append(temp)
        if temp == "G":
            found = True
            break
        if depth == limit:
            continue
        for child in reversed(graph[temp]):
            stack.append((child, depth + 1))
    print(stack, visited)
    if found:
        print(f"Limit {limit} -> FOUND, visited: {visited}")
    else:
        print(f"Limit {limit} -> CUTOFF, visited: {visited}")

for limit in [1, 2, 3, 4]:
    dls("A", limit)
    print()
