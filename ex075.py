countp = 0
n = (int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')))
print(f'Você digitou os valores {n}')
print(f'O 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O 3 apareceu na {n.index(3)+1}ª posição')
else:
    print('O número 3 não apareceu')
print('Os valores pares digitados foram: ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
