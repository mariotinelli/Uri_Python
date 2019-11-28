entrada = int(input())
anos = meses = 0

while entrada >= 30:
    if entrada >= 365:
        anos+=1
        entrada-=365
    elif entrada >= 30:
        meses+=1
        entrada-=30

print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(entrada))