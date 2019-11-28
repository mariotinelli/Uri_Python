n = int(input())

for i in range(n):

    dieta = input()
    manha = input()
    almoco = input()
    lista_dieta = []
    ingerido = ''
    jantar = ''

    for indice in dieta:
        lista_dieta.append(indice)

    lista_dieta = lista_dieta.sort()



    for indice in manha:
        for indice2 in lista_dieta:
            if indice == indice2:
                ingerido += indice
    for indice in almoco:
        for indice2 in lista_dieta:
            if indice == indice2:
                ingerido += indice

    for indice in lista_dieta:
        for indice2 in ingerido:
            if indice not in ingerido:
                if indice not in jantar:
                    jantar += indice

    comparador = (jantar + manha + almoco) == dieta

    if not comparador:
        print('CHEATER')
    elif jantar == '':
        print(*lista_dieta, sep='')
    else:
        print(jantar)
