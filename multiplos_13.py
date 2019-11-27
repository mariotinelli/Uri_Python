x = int(input())
y = int(input())
soma = 0
if x < y:
    cont = x
    while cont <= y:
        if cont % 13 != 0:
            soma += cont

        cont += 1
else:
    cont = y
    while cont <= x:
        if cont % 13 != 0:
            soma += cont

        cont += 1


print(soma)