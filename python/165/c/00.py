import itertools


n, m, q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(q)]
ans = 0

nums = list(range(1, m+1))
seqs = list(itertools.combinations_with_replacement(nums, n))

for seq in seqs:
    point = 0
    for query in queries:
        a, b, c, d = query
        if seq[b-1] - seq[a-1] == c:
            point += d
    if point > ans:
        ans = point

print(ans)
