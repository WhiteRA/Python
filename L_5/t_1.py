a = int(input("Число - "))
b = int(input("Степень - "))


def level(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / (a * level(a, -b - 1))
    else:
        return a * level(a, b - 1)


print(level(a, b))
