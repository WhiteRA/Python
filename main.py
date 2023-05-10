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

# Найдите повторяющееся число в заданном целочисленном массиве. Все остальные элементы массива различны.
q = [int(i) for i in input().split()]
a = []
for i in range(len(q)):
    if q.count(i) > 1:
        if i not in a:
            a.append(i)
print(a)
