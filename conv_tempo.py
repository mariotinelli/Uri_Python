entrada = int(input())
horas = minutos = 0

while entrada > 60:
    if entrada > 3600:
        horas+=1
        entrada-=3600
    elif entrada > 60:
        minutos+=1
        entrada-=60

print('{}:{}:{}'.format(horas, minutos, entrada))