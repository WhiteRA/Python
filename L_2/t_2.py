S = int(input())
P = int(input())
i = 0
j = 0
while i < S:
    while j < P:
        if i + j == S and i * j == P:
            break
        j+=1
    i+=1
print(int(i/2), int(j/2))