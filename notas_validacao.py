

opcao = 1

while opcao == 1:
    cont = 0
    media = 0
    while cont < 2:
        x = float(input())
        if 0 <= x <= 10:
            cont+=1
            media+=x
        else:
            print('nota invalida')
    media = media / 2
    print('media = {:.2f}'.format(media))
    while opcao != 2:
        opcao = int(input('novo calculo (1-sim 2-nao)'))
        if opcao == 1:
            break



