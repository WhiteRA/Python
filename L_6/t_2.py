import random

"""
min = int(input("MIN - "))
max = int(input("MAX - "))
list = []
for i in range(20):
    list.append(random.randint(-20, 20))
    i += 1
print(*list)
"""

min = int(input("MIN - "))
max = int(input("MAX - "))
list_1 = [random.randint(1, 20) for i in range(20)]
print(*list_1)
list_2 = [i for i in range(20) if list_1[i] >= min and list_1[i] <= max]
print(f"Номера элементов в заданном диапазоне - {list_2}")
