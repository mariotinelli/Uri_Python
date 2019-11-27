
entrada = input().split()
x = int(entrada[0])
y = int(entrada[1])


cont2 = 1
while cont2 <= y:
    cont1 = 0
    while cont1 < x:
        if not cont1+1 == x:
            print(cont2+cont1, end=' ')
        else:
            print(cont2+cont1, end='' )
        cont1+=1

    cont2+=x
    print(end="\n")