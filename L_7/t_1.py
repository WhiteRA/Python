def rhythm(str):
    str = str.split()
    print(str)
    list_1 = []
    for a in str:
        sum_w = 0
        for i in a:
            if i in "аеёиоуыэюя":
                sum_w += 1
        list_1.append(sum_w)
    return len(list_1) == list_1.count(list_1[0])


str_1 = "пара-ра-рам рам-пам-папам па-ра-па-дам"
if rhythm(str_1):
    print("Парам пам-пам")
else:
    print("Пам парам")
