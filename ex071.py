n = int(input('Qual valor você gostaria de sacar? R$ '))
notas50 = 0
notas20 = 0
notas10 = 0
notas1 = 0
while True:
    if n // 50 > 0:
        notas50 = n // 50
        resto = n % 50
    if resto // 20 > 0:
        notas20 = resto//20
        resto = n % 20
    if resto // 10 > 0:
        notas10 = resto//10
        resto = n % 10
    if resto // 1 > 0:
        notas1 = resto//1
        resto = n % 1
    if resto == 0:
        break
if notas50 > 0:
    print(f'Total de {notas50} cédulas de R$ 50')
if notas20 > 0:
    print(f'Total de {notas20} cédulas de R$ 20')
if notas10 > 0:
    print(f'Total de {notas10} cédulas de R$ 10')
if notas1 > 0:
    print(f'Total de {notas1} cédulas de R$ 1')
