import re

try:
    while True:

        linha1 = input()
        linha2 = input()

        tam = 0

        if linha1 == '' or linha2 == '':
            break



        for i in range(len(linha1)):
            for j in range(len(linha1)):
                result = re.match('(.{i,j})', linha2)
        print(result)

        print(tam)
        #for i in range(len(linha1)):
         #   for indice in range(len(linha1)):
          #      for j in range(len(linha2)):
           #         for indice2 in range(len(linha2)):
            #            print(linha1[j:indice+1])
             #           print(linha2[i:indice2])
              #          print('---')
               #         if linha1[j:indice+1] == linha2[i:indice2]:
                #            tam = indice
       # print(tam)

        break
except EOFError:
    pass
