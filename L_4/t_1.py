n = int(input("Ввод числа N - "))
# m = int(input("Ввод числа M - "))
list_0 = set()
# list_1 = set()
print()
print(
    "ВНИМАНИЕ ! В данном коде используются множества которые не могую хранить повторяющиеся элементы !"
)
print("Числа не должны повторятся !")
print()
for i in range(n):
    a = list_0.add(int(input("Ввод числа первого множества - ")))
    x = 0
    if x == a:
        print("Такое число уже есть")
    else:
        x += 1
        print("Тута")
        break


print(*list_0)  # Звёздочка нужна для того чтоб вывод был без фигурных скобок
print()
"""
for j in range(m):
    list_1.add(int(input("Ввод числа второго множества - ")))
print(*list_1)
print()
"""
