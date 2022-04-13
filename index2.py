n = 5
pairs1 = [(0, 1), (2, 1), (2, 3), (3, 4), (4, 0)]
pairs2 = [(0, 1), (2, 1), (2, 3), (3, 4), (4, 0), (4, 2)]

# Ref: https://www.youtube.com/watch?v=0dJmTuMrUZM
# 但是并没有完全参考它的。比如它有 backtracking，我的实现没有，因为我 clone 了 visited。
# 视频例子后面的实现其实也没有包含backtracking的内容，因为C++是pass by value的。
# 思路上要把大问题变成多个小问题。比如说要对每个节点作为起点visit一次，那就定义出一个新的function
# 这个问题是DFS，因为用了递归，所以是深度优先的。

def visit(pairs, start, visited):
    if start in visited:
        return True
    visited.add(start)
    for node in [node for (dep, node) in pairs if dep == start]:
        if(visit(pairs, node, visited.copy())):
            return True
    return False

def has_cycle(pairs):
    for i in range(n):
        if visit(pairs, i, set()):
            return True
    return False

print(has_cycle(pairs1))
print(has_cycle(pairs2))
