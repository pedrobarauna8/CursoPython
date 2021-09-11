casa = int(input('Valor da casa: '))
salario = int(input('Salário: '))
anos = int(input('Quantos anos de financiamento? '))
print('Para pagar uma casa de {} em {} anos a prestação será de {:2f} reais'.format(casa, anos, (casa/(anos*12))))
if (casa/(anos*12)) < (salario*0.30):
    print('FINANCIAMENTO APROVADO! ')
else:
    print('FINANCIAMENTO NEGADO! ')
