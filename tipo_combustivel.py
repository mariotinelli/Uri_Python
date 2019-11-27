
alcool = 0
gasolina = 0
diesel = 0

print('MUITO OBRIGADO')
while True:
    while True:
        opcao = int(input())
        if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
            break
    if opcao == 4:
        break
    elif opcao == 1:
        alcool+=1
    elif opcao == 2:
        gasolina+=1
    elif opcao == 3:
        diesel+=1

print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(diesel))



