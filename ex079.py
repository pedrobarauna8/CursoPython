lista = list()
r = ''
while r in 'Ss':
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Número adicionado.')
    else:
        print('Número repetido, não vou adicionar.')
    r = str(input('Quer continuar? [S/N] '))
lista.sort()
print(f'Você digitou os valores {lista}')
