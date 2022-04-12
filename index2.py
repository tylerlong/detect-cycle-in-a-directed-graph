n = 5
pairs1 = [(0, 1), (2, 1), (2, 3), (3, 4), (4, 0)]
pairs2 = [(0, 1), (2, 1), (2, 3), (3, 4), (4, 0), (4, 2)]

visited = [False] * 5
def visit(pairs, start, visited):
    if visited[start]:
        return True
    visited[start] = True
    for node in [node for (dep, node) in pairs if dep == start]:
        if(visit(pairs, node, visited[:])):
            return True
    return False

def has_cycle(pairs):
    for i in range(n):
        if visit(pairs, i, [False] * n):
            return True
    return False

print(has_cycle(pairs1))
print(has_cycle(pairs2))
