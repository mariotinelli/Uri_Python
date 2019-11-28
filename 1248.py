def cria_lista(string):
    nova_lista = []
    for indice in string:
        nova_lista.append(indice)
    return nova_lista


def cria_string(lista):
    nova_string = ''
    for i in lista:
        nova_string += i
    return nova_string


n = int(input())

for i in range(n):

    dieta = input()
    manha = input()
    almoco = input()
    lista_dieta = []
    ingerido = ''
    jantar = ''

    lista_dieta = cria_lista(dieta)
    lista_dieta.sort()
    dieta = cria_string(lista_dieta)

    cheater = 0

    for indice in manha:
        for indice2 in lista_dieta:
            if indice not in lista_dieta:
                cheater = 1
            elif indice == indice2:
                ingerido += indice
    for indice in almoco:
        for indice2 in lista_dieta:
            if indice not in lista_dieta:
                cheater = 1
            elif indice == indice2:
                ingerido += indice

    for indice in lista_dieta:
        for indice2 in ingerido:
            if indice not in ingerido:
                if indice not in jantar:
                    jantar += indice

    lista_ingerido = cria_lista(ingerido)
    lista_ingerido.sort()
    ingerido = cria_string(lista_ingerido)

    lista_jantar = cria_lista(jantar)
    lista_jantar.sort()

    if cheater == 0:
        if jantar == '':
            if ingerido == dieta:
                print('')
            else:
                print(cria_string(lista_dieta).upper())
        elif lista_jantar:
            print(cria_string(lista_jantar).upper())
    else:
        print('CHEATER')

