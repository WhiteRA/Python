a = int(100)
print ((int(a / 100))+(int((a % 100) / 10))+(int(a % 10)))

a = int(input())
print((a//6), ((a//6)*4), (a//6))

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

n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
