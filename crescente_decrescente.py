

while True:
    entrada = [int(i) for i in input().split()]
    x = entrada[0]
    y = entrada[1]

    if x > y:
        print('Decrescente')
    elif x < y:
        print('Crescente')
    else:
        break