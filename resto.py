x = int(input())
y = int(input())
ls = []
if x < y:
    cont = x+1
    while cont < y:
        if cont % 5 == 2 or cont % 5 == 3:
            ls.append(cont)

        cont += 1
else:
    cont = y+1
    while cont < x:
        if cont % 5 == 2 or cont % 5 == 3:
            ls.append(cont)

        cont += 1

print(*ls, sep='\n')

