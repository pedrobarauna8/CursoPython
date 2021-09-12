import random

cont = 0
print('-=-' *20)
print('Vou pensar em um número entre 0 e 10. Tente acertar')
print('-=-' *20)
n = random.randint(0,10)
print(n)
nu = int(input('Qual número eu pensei? '))
if n == nu:
    print('Você acertou! ')
else:
    print('Você errou. Tente Novamente! ')
    while not n == nu:
        nu = int(input('Qual número eu pensei? '))
        if n == nu:
            print('Você acertou! ')
        else:
            print('Você errou! ')
            cont += 1
str(print('Eu pensei no número {} e você precisou de {} tentativas'.format(n, cont + 1)))
