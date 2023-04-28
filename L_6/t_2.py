import random


list_1 = [random.randint(-5, 20) for i in range(20)]
print(*list_1)
print()
min = int(input("MIN - "))
max = int(input("MAX - "))
list_2 = [i for i in range(20) if list_1[i] >= min and list_1[i] <= max]
print(f"Номера элементов в заданном диапазоне - {list_2}")
