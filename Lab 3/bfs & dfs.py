graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

visited = []
queue = []

def bfs(node):
    queue.append(node)
    while queue:
        print(queue, visited)
        temp = queue.pop(0)
        visited.append(temp)
        if temp == "G":
            break
        for child in graph[temp]:
            queue.append(child)

bfs("A")
print(queue, visited)

visited = []
stack = []

def dfs(node):
    stack.append(node)
    while stack:
        print(stack, visited)
        temp = stack.pop()
        visited.append(temp)
        if temp == "G":
            break
        for child in reversed(graph[temp]):
            stack.append(child)

dfs("A")
print(stack, visited)
