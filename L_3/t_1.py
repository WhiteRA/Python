list_0 = []
q = int(input("Число элемнтов - "))
w = int(input("Искомый элемент - "))
for i in range(q):
    list_0.append(i + 1)
print(list_0)
x = 0
for l in range(q):
    if l == w:
        x += 1
print(f"Это число встречается {x} раз")
