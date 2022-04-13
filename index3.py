n = 5
pairs1 = [(0, 1), (2, 1), (2, 3), (3, 4), (4, 0)]
pairs2 = [(0, 1), (2, 1), (2, 3), (3, 4), (4, 0), (4, 2)]

# 这里BFS的版本也能得出正确结果。所以关键不在于 DFS 还是 BFS，关键在于，你得每一轮都要 clone visited
# 这是因为，对于某个round 的节点，并不是之前的 round 访问过的节点都是 dependency。共享一个 visited 的算法是错误的
# 这里的 visited 可以是 array 也可以是 set。 set的话通用性更好些。 

def has_cycle(pairs):
    unprocessed = set(range(n))
    while len(unprocessed) > 0:
        current = [(unprocessed.pop(), set())]
        while len(current) > 0:
            next = []
            for (node, visited) in current:
                if node in visited:
                    return True
                visited.add(node)
                if node in unprocessed:
                    unprocessed.remove(node)
                next += [(i, visited.copy()) for (pre, i) in pairs if pre == node]
            current = next
    return False

print(has_cycle(pairs1))
print(has_cycle(pairs2))
