class Observatory:
    def __init__(self, height):
        self.height = height
        self.around = []

    def is_good(self, li, di):
        flag = True
        for i in self.around:
            oo = li[i - 1]
            if oo.height >= self.height:
                flag = False
            else:
                di[i - 1] = False
        return flag


n, m = map(int, input().split())
h = [int(i) for i in input().split()]
observatories = [Observatory(h[i]) for i in range(n)]
dic = {}
for i in range(n):
    dic[i] = True

for i in range(m):
    a, b = map(int, input().split())
    observatories[a - 1].around.append(b)
    observatories[b - 1].around.append(a)

ans = 0

for i in range(n):
    o = observatories[i]
    if dic[i]:
        if o.is_good(observatories, dic):
            ans += 1

print(ans)
