pessoas = list()
lista = list()
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    lista.append(pessoas[:])
    pessoas.clear()
    r = str(input('Quer continuar? [S/N] '))
    if r not in 'Ss':
        break
print(f'{len(lista)} pessoas foram cadastradas.')
print(f'O maior peso é de {maior} ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]')
print(f'O menor peso é de {menor} ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')