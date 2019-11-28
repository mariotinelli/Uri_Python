
try:
    while True:

        entrada = input()
        if entrada == '':
            break
        entrada2 = input()
        if entrada2 == '':
            break

        tam = 0
        len1 = len(entrada)+1
        len2 = len(entrada2)+1

        for i in range(len1):
            for indice1 in range(len1):
                for j in range(len2):
                    for indice2 in range(len2):
                        if indice1 > 0 and indice2 > 0 and i < indice1 and j < indice2:
                            if entrada[i:indice1] == entrada2[j:indice2] and len(entrada[i:indice1]) > tam:
                                tam = len(entrada[i:indice1])
        print(tam)

except EOFError:
    pass
