lista = list()
dict = dict()
media = 0
while True:
    dict['Nome'] = str(input('Nome: '))
    dict['Sexo'] = str(input('Sexo: [M/F] '))
    dict['Idade'] = int(input('Idade: '))
    lista.append(dict.copy())
    del dict['Nome']
    del dict['Sexo']
    del dict['Idade']
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'Total de pessoas cadastradas: {len(lista)}')
for c in range(0, len(lista)):
    media += (lista[c]['Idade'])/len(lista)
print(f'Média de idade: {media:.2f}')
print('Mulheres cadastradas: ', end=' ')
for c in range(0, len(lista)):
    if lista[c]['Sexo'] in 'Ff':
        print(f'{lista[c]["Nome"]}', end=' ')
print('\nPessoas com idade acima da média: ', end='')
for c in range(0, len(lista)):
    if lista[c]['Idade'] > media:
        print(f'{lista[c]["Nome"]}', end='')
