n = int(input())
s = [input() for _ in range(n)]

dic = {}
for i in range(n):
    dic[s[i]] = 0

print(len(dic.keys()))
