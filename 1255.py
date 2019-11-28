
n = int(input())


def ordenaSaida(string):
    lista = []
    for i in string:
        lista.append(i)
    lista.sort()
    nova_string = ''
    for i in lista:
        nova_string += i
    return nova_string


while n >= 0:

    entrada = input()
    entrada = entrada.lower().strip()
    lista = []
    maior = 0
    saida = ''

    for i in entrada:
        qtd_vezes = entrada.count(i)
        if qtd_vezes > maior:
            maior = qtd_vezes

    for i in range(len(entrada)):
        if entrada[i] != ' ' and entrada[i] not in saida:
            vezes = entrada.count(entrada[i])
            if vezes == maior:
                saida += entrada[i]
    saida = ordenaSaida(saida)
    print(saida)

    n -= 1