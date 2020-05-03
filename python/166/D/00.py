x = int(input())
r = range(-500, 501)

flag = False

for i in r:
    for j in r:
        if i**5 - j**5 == x:
            print(i, j)
            flag = True
            break
    if flag:
        break
