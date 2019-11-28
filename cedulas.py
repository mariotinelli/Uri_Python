entrada = int(input())
nota100 = nota50 = nota20 = nota10 = nota5 = nota2 = nota1 = 0
print(entrada)
while (entrada > 0):
    if entrada >= 100:
        nota100+=1
        entrada-=100
    elif entrada >= 50:
        nota50+=1
        entrada-=50
    elif entrada >= 20:
        nota20+=1
        entrada-=20
    elif entrada >= 10:
        nota10+=1
        entrada-=10
    elif entrada >= 5:
        nota5+=1
        entrada-=5
    elif entrada >= 2:
        nota2+=1
        entrada-=2
    else:
        nota1+=1
        entrada-=1

print('{} nota(s) de R$ 100,00'.format(nota100))
print('{} nota(s) de R$ 50,00'.format(nota50))
print('{} nota(s) de R$ 20,00'.format(nota20))
print('{} nota(s) de R$ 10,00'.format(nota10))
print('{} nota(s) de R$ 5,00'.format(nota5))
print('{} nota(s) de R$ 2,00'.format(nota2))
print('{} nota(s) de R$ 1,00'.format(nota1))

