n, m = map(int, input().split())
A = list(map(int, input().split()))

print(max(n-sum(A), -1))
