
opcao = 1
cont_inter = 0
cont_gremio = 0
empate = 0
total = 0
while opcao == 1:

    entrada = input().split()
    inter = int(entrada[0])
    gremio = int(entrada[1])

    total+=1

    if inter > gremio:
        cont_inter+=1
    elif inter == gremio:
        empate+=1
    else:
        cont_gremio+=1
    while True:
        opcao = int(input('Novo grenal (1-sim 2-nao)'))
        if opcao == 2 or opcao == 1:
            break

print('{} grenais'.format(total))
print('Inter:{}'.format(cont_inter))
print('Gremio:{}'.format(cont_gremio))
print('Empates:{}'.format(empate))
if cont_gremio > cont_inter:
    print('Gremio venceu mais')
elif cont_gremio < cont_inter:
    print('Inter venceu mais')
else:
    print('Nao houve vencedor')
