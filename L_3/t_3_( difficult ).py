# Я не стал делать ещё один словарь для англ.яза - по сути то-же самое только буквы другие.
# Хотелось бы разобрать это задание на уроке - какие более простые способы заполнения словаря можно реализовать.
#   А то писать его руками ваще не круто )
dtr_eng = {}
dtr_eng.update(
    {
        "а": "1",
        "в": "1",
        "е": "1",
        "и": "1",
        "н": "1",
        "о": "1",
        "р": "1",
        "с": "1",
        "т": "1",
        "д": "2",
        "к": "2",
        "л": "2",
        "м": "2",
        "п": "2",
        "у": "2",
        "б": "3",
        "г": "3",
        "ё": "3",
        "ь": "3",
        "я": "3",
        "й": "4",
        "ы": "4",
        "ж": "5",
        "з": "5",
        "ч": "5",
        "ц": "5",
        "ч": "5",
        "ш": "8",
        "э": "8",
        "ю": "8",
        "ф": "10",
        "щ": "10",
        "ъ": "10",
        "т": "1",
        "т": "1",
        "т": "1",
    },
)
j = 0
str_in = input("Ввод слова - ")
for i in range(len(str_in)):
    j += int(dtr_eng.get(str_in[i]))
print(f" Вес введённого слова = {j}")
