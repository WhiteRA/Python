q = int(input("Степень - "))
a = int(input('Число - '))
i = 1
print(1)
while i <= q:
    i *= a
    if i>=q:
        break
    print(i)