countmenor = 0
countmaior = 0
for c in range(1,8):
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    if ano <= 2003:
        countmaior += 1
    else:
        countmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade e {} menores'.format(countmaior, countmenor))
