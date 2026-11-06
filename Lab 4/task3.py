graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": [],
}

h_over = {"S": 5, "A": 4, "B": 4, "C": 10, "G": 0}

visited = []
pqueue = []


def astar(node, heuristic):
    best = {node: 0}
    pqueue.append((0 + heuristic[node], 0, node, [node]))
    while pqueue:
        pqueue.sort()
        print(pqueue, visited)
        f, cost, temp, path = pqueue.pop(0)
        if cost != best[temp]:
            continue
        visited.append(temp)
        if temp == "G":
            print("Goal found! Path:", path, "Total cost:", cost)
            return path, cost
        for child, weight in graph[temp]:
            g_new = cost + weight
            if g_new < best.get(child, float("inf")):
                best[child] = g_new
                f_new = g_new + heuristic[child]
                pqueue.append((f_new, g_new, child, path + [child]))


print("===== A* with overestimate h(C)=10 =====")
visited = []
pqueue = []
astar("S", h_over)
print("pqueue, visited")
