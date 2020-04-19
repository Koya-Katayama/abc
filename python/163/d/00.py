n, k = map(int, input().split())
mod = 10**9+7
ans = 0

for i in range(k, n+2):
    l = i*(i-1)//2 
    r = i*(2*n-i+1)//2
    ans = (ans+r-l+1)%mod

print(ans)
