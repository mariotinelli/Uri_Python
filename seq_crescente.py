
while True:
    opcao = int(input())
    if opcao == 0:
        break
    cont = 1
    ls = []
    while cont <= opcao:
        ls.append(cont)
        cont+=1
    print(*ls, sep=" ", end='\n')
