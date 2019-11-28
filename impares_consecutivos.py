n = int(input())
cont = 0
while cont < n:
    total = 0
    entrada = input().split()
    x = int(entrada[0])
    y = int(entrada[1])
    if x < y:
        cont2 = x+1
        while cont2 < y:
            if cont2 % 2 != 0:
                total+=cont2
            cont2+=1
    else:
        cont2 = y+1
        while cont2 < x:
            if cont2 % 2 != 0:
                total+=cont2
            cont2 += 1
    print(total)
    cont+=1
