n, k = map(int, input().split())
d = [0]*k
a = [None]*k
okashi = {}

for i in range(k):
    dd = int(input())
    aa = [int(j) for j in input().split()]
    d[i] = dd
    a[i] = aa

for i in range(1, n+1):
    okashi[i] = 0

for i in range(k):
    for aaa in a[i]:
        okashi[aaa] += 1

ans = 0

for times in okashi.values():
    if times == 0:
        ans += 1

print(ans)
