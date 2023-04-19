list_0 = []
q = int(input("Число элемнтов - "))
w = int(input("Искомый элемент - "))
for i in range(q):
    list_0.append(i + 1)
print(list_0)

for j in range(q + 1):
    if list_0[j] == w:
        print(f"Самые близкие по величине элемент {list_0[j + 1]}")
    else:
        if list_0[j] < w:
            print(f"Самые близкие по величине элемент {list_0[j - 1]}")
            break
