from random import randint
n = (randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os números sorteados foram: ', end='')
for c in n:
    print(f'{c} ', end='')
print(f'\nO maior número foi: {max(n)}')
print(f'O maior número foi: {min(n)}')

