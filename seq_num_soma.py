

while True:
    entrada = input().split()
    m = int(entrada[0])
    n = int(entrada[1])
    if m != 0 and n != 0:
        ls = []
        if m > n:
            cont = n
            sum = 0
            while cont <= m:
                ls.append(cont)
                sum+=cont
                cont+=1
        else:
            cont = m
            sum = 0
            while cont <= n:
                ls.append(cont)
                sum += cont
                cont += 1
        print(*ls, sep=' ', end='')
        print(' Sum={}'.format(sum))
    else:
        break
