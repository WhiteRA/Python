import random

"""
# Найдите недостающее число от 1 до 100 в заданном целочисленном массиве с 100 элементами, используя только один цикл от 1 до 100.
q = list(map(int, input().split()))
a = 0
for i in range(len(q)):
    a = q[i] + a
a = 5050 - a
print(a)

if q.count(i) > 1:
        if i not in a:
            a.append(i)
"""
list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
q = []
z = {}


def chetn(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            q.append(a[i])
    print(q)


def kvadr(a):
    for i in range(len(a)):
        z[a[i]] = a[i] * a[i]
    print(z)


chetn(list_1)
kvadr(q)
