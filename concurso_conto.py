import sys

while True:
    entrada = input().split()
    if entrada == '':
        break
    conto = input()
    if 2 <= entrada[0] <= 1000:
        n = int(entrada[0])  # numero de palavras
    else: break
    if 1 <= int(entrada[1] <= 30):
        num_l = int(entrada[1])  # numero maximo de linhas por pagina
    else: break
    if 1 <= entrada[2] <= 70:
        c = int(entrada[2])  # numero maximo de caracteres por linha
    else: break
    if len(conto) > n:
        break

    num_caracteres = len(conto)

    lista = conto.split()
    num_palavras = len(lista)

    num_linhas = num_caracteres / c
    paginas = 1

    while num_linhas > num_l:
        paginas += 1
        num_linhas -= num_l

    print(paginas)

