count18 = countm = countm20 = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        count18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        countm += 1
    if sexo == 'F' and idade < 20:
        countm20 += 1
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {count18}')
print(f'Total de homens: {countm}')
print(f'Total de mulheres com menos de 20 anos: {countm20}')
