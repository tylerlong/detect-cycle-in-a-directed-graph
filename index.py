n = 5
pairs1 = [(0, 1), (2, 1), (2, 3), (3, 4), (4, 0)]
pairs2 = [(0, 1), (2, 1), (2, 3), (3, 4), (4, 0), (4, 2)]

# dynamic programming, I figured out this solution and I think it is the best
def has_cycle(pairs):
    dp = dict([(i, set()) for i in range(n)])
    for (dep, node) in pairs:
        if node in dp[dep]:
            return True
        dp[node].add(dep)
        dp[node] = dp[node].union(dp[dep])
    return False

print(has_cycle(pairs1))
print(has_cycle(pairs2))
