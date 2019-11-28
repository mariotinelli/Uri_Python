
n = int(input())

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
alfabeto = alfabeto.upper()

for index in range(n):

    palavra = input()
    qtd_casas = int(input())
    nova_palavra = ''
    pos = 0
    nova_pos = 0

    for indice in palavra:
        pos = alfabeto.find(indice)
        if pos > qtd_casas:
            nova_pos = pos - qtd_casas
        else:
            nova_pos = (pos - qtd_casas) + 26
            if nova_pos >= 26:
                nova_pos = 0
        nova_palavra += alfabeto[nova_pos]

    print(nova_palavra)
