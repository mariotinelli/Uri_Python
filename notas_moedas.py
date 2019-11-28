entrada = float(input())
nota100 = nota50 = nota20 = nota10 = nota5 = nota2 = nota1 = 0
nota05 = nota025 = nota01 = nota005 = nota001 = 0

while (entrada >= 0.05):
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
    elif entrada >= 1:
        nota1+=1
        entrada-=1
    elif entrada >= 0.5:
        nota05+=1
        entrada-=0.5
    elif entrada >= 0.25:
        nota025+=1
        entrada-=0.25
    elif entrada >= 0.10:
        nota01+=1
        entrada-=0.10
    elif entrada >= 0.05:
        nota005+=1
        entrada-=0.05

while entrada >= 0.01:
    nota001+=1
    entrada-=0.01


print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(nota100))
print('{} nota(s) de R$ 50.00'.format(nota50))
print('{} nota(s) de R$ 20.00'.format(nota20))
print('{} nota(s) de R$ 10.00'.format(nota10))
print('{} nota(s) de R$ 5.00'.format(nota5))
print('{} nota(s) de R$ 2.00'.format(nota2))

print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(nota1))
print('{} moeda(s) de R$ 0.50'.format(nota05))
print('{} moeda(s) de R$ 0.25'.format(nota025))
print('{} moeda(s) de R$ 0.10'.format(nota01))
print('{} moeda(s) de R$ 0.05'.format(nota005))
print('{} moeda(s) de R$ 0.01'.format(nota001))


