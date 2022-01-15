lista = []
listap = []
listai = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)
    r = str(input('Quer continuar? [S/N] '))
    if r not in 'Ss':
        break
print(f'Esses foram os números digitados: {lista}')
print(f'Esses foram os números pares digitados: {listap}')
print(f'Esses foram os números ímpares digitados: {listai}')
