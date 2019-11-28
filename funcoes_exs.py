def saudacao(saudacao='Olá', nome='usuário'):
    return saudacao, nome


def soma(a, b, c):
    return a + b + c


def percentual(num, percentual):
    return num + ((percentual / 100) * num)


def fizzbuzz(num):
    if num % 5 == 0 and num % 3 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return num


print(saudacao('Ola', 'Mario'))
print(soma(5, 5, 5))
print(percentual(100, 10))
print(fizzbuzz(7))

