import random

"""
# Найдите недостающее число от 1 до 100 в заданном целочисленном массиве с 100 элементами, используя только один цикл от 1 до 100.
q = list(map(int, input().split()))
a = 0
for i in range(len(q)):
    a = q[i] + a
a = 5050 - a
print(a)
"""
q = [int(i) for i in input().split()]
q = sorted(q)
print(q)
for i in range(len(q)):
    if q[i] == q[i + 1] and i < len(q):
        print(q[i])
