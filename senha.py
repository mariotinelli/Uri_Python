
senha = False
senha_fixa = 2002
while not senha:
    entrada = int(input())

    if entrada == 2002:
        print('Acesso Permitido')
        senha = True
    else:
        print('Senha Invalida')

