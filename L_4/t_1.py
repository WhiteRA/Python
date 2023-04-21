n = int(input("Ввод числа N - "))
m = int(input("Ввод числа M - "))
plenty_0 = set()
plenty_1 = set()
print()
print(
    "ВНИМАНИЕ ! В данном коде используются множества которые не могую хранить повторяющиеся элементы !"
)
print("Числа не должны повторятся !")
print()

for i in range(n):
    a = plenty_0.add(int(input("Ввод числа первого множества - ")))
print(*plenty_0)  # Звёздочка нужна для того чтоб вывод был без фигурных скобок
print()

for j in range(m):
    plenty_1.add(int(input("Ввод числа второго множества - ")))
print(*plenty_1)
print()

list_0 = sorted(plenty_0.union(plenty_1))
print(*list_0)
