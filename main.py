o = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 30)]
def orb(o):
    q = {}
    a = 0
    for i in o:
        if i[0] == i[1]:
            a = a
        else:
            q[i[0]*i[1]] = i
            for key in q:
                if a < key:
                    a = key
    return q.get(a)
print(orb(o))