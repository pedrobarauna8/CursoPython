lista = []
count = 0
while True:
    lista.append(int(input('Digite um número: ')))
    count += 1
    r = str(input('Quer continuar? [S/N] '))
    if r not in 'Ss':
        break
lista.sort(reverse=True)
print(f'{count} números foram digitados. Os valores em ordem decresente é {lista}')
if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista!')
