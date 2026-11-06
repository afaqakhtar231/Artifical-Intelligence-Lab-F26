import math

scores = [1, 2, 3, 4, 5, 6, 7, 8]
treeDepth = math.log2(len(scores))
leaves = 0

def minmax(currDepth, nodeIndex, isMaxTurn):
    global leaves
    if currDepth == treeDepth:
        leaves += 1
        return scores[nodeIndex]

    if isMaxTurn:
        return max(
            minmax(currDepth + 1, nodeIndex * 2, False),
            minmax(currDepth + 1, nodeIndex * 2 + 1, False)
        )
    else:
        return min(
            minmax(currDepth + 1, nodeIndex * 2, True),
            minmax(currDepth + 1, nodeIndex * 2 + 1, True)
        )

def alphabeta(currDepth, nodeIndex, isMaxTurn, alpha, beta):
    global leaves
    if currDepth == treeDepth:
        leaves += 1
        return scores[nodeIndex]

    if isMaxTurn:
        best = float('-inf')
        best = max(best, alphabeta(currDepth + 1, nodeIndex * 2, False, alpha, beta))
        alpha = max(alpha, best)
        if alpha >= beta:
            return best  # prune!
        best = max(best, alphabeta(currDepth + 1, nodeIndex * 2 + 1, False, alpha, beta))
        return best
    else:
        best = float('inf')
        best = min(best, alphabeta(currDepth + 1, nodeIndex * 2, True, alpha, beta))
        beta = min(beta, best)
        if alpha >= beta:
            return best  # prune!
        best = min(best, alphabeta(currDepth + 1, nodeIndex * 2 + 1, True, alpha, beta))
        return best

orders = [
    ("Original",   [1, 2, 3, 4, 5, 6, 7, 8]),
    ("Good order", [5, 6, 7, 8, 1, 2, 3, 4]),
    ("Bad order",  [3, 4, 1, 2, 7, 8, 5, 6])
]

for name, s in orders:
    scores = s
    treeDepth = math.log2(len(scores))

    leaves = 0
    print(name, "-> Minimax:", minmax(0, 0, True), "| Leaves:", leaves)

    leaves = 0
    print(name, "-> AlphaBeta:", alphabeta(0, 0, True, float('-inf'), float('inf')), "| Leaves:", leaves)
