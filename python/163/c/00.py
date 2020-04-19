n = int(input())
a = input().split()
 
joshi = {}
 
for i in range(1, n+1):
    joshi[str(i)] = 0
 
for i in range(n-1):
    joshi[a[i]] += 1
 
for ans in joshi.values():
    print(ans)
