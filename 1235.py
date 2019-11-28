
n = int(input())

for i in range(n):

    entrada = input()
    tam = len(entrada)
    tam_esq = tam//2
    tam_dir = tam - tam_esq

    nova_string = ''

    for metade_esq in range(tam_esq-1, -1, -1):
        nova_string += entrada[metade_esq]
    for metade_dir in range(tam-1, tam_dir-1, -1):
        nova_string += entrada[metade_dir]
    print(nova_string)