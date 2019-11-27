
while True:

    entrada = input()
    if entrada == '':
        break
    nova_entrada = ''

    for indice in range(len(entrada)):
        if entrada[indice] != ' ':
            if indice % 2 == 0:
                nova_entrada += entrada[indice].upper()
            else:
                nova_entrada += entrada[indice].lower()
        else:
            nova_entrada += entrada[indice]
    print(nova_entrada)
