a = int(385967)
q = int(a % 10)
w = int(a % 100 /10)
e = int(a % 1000 /100)
z = q + w + e
f = int(a // 100000)
v = int(a // 10000) % 10
g = int(a // 1000) % 10
n = f + v + g
if z == n:
    print('YES')
else:
    print('NO')