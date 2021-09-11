import random
import time
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente acertar')
print('-=-' *20)
n = random.randint(0,5)
nu = int(input('Qual número eu pensei? '))
print('PROCESSANDO...')
time.sleep(1)
if n == nu:
    print('Você acertou! ')
else:
    print('Você errou! ')
str(print('Eu pensei no número {}'.format(n)))
