import random
n = int(input())
k = 0
for i in range(n):
    v = int(random.randint(0, 1))
    if v == 1:
        k += 1
if k < n / 2:
    print(k)
else:
    print(n-k)