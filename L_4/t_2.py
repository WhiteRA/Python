from random import randint

# Использовал рандомайзер для красоты
list_0 = []
q = int(input("Колличество кустов - "))
print()
for i in range(q):
    list_0.append(randint(0, 100))
print(list_0)
print()
w = int(input("Номер куста - "))
sum = 0

if w > q:
    print("Такого куста нет")
else:
    sum = list_0[w] + list_0[w - 1] + list_0[w + 1]
    print(f"Колличество ягод - {sum}")
