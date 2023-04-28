import random

list_1 = [random.randint(-5, 10) for i in range(10)]
print(*list_1)
print()
down = int(input("MIN - "))
up = int(input("MAX - "))
if down >= min(list_1) and up <= max(list_1):
    list_2 = [i for i in range(20) if list_1[i] >= down and list_1[i] <= up]
    print(f"Номера элементов в заданном диапазоне - {list_2}")
else:
    print("Введено значение выходящее за список")
