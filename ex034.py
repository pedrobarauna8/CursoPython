salario = float(input('Qual é o seu salário atual? '))
if salario >= 1250:
    novosalario = salario * 1.10
    print('O seu novo salário será de: R${:.2f}'.format(novosalario))
else:
    novosalario = salario *1.15
    print('O seu novo salário será de: R${:.2f}'.format(novosalario))
