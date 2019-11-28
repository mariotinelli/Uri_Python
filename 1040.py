entrada = input().split()

n1 = (float(entrada[0]))*0.2
n2 = (float(entrada[1]))*0.3
n3 = (float(entrada[2]))*0.4
n4 = (float(entrada[3]))*0.1

media = n1+n2+n3+n4
print('Media: {:.1f}'.format(media))
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif 5.0 <= media < 7.0:
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: {:.1f}'.format(exame))
    nota_final = (exame+media)/2
    if nota_final >= 5.0:
        print('Aluno aprovado.')
    elif nota_final < 5.0:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(nota_final))