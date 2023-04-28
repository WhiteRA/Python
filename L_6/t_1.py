q = int(input("Начальное число прогрессии - "))
a = int(input("Разность  - "))
NL = [q + (i - 1) * a for i in range(1, int(input("Количество элементов - ")) + 1)]
print(NL)
