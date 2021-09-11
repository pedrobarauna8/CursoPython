d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km rodados? '))
print('O total a pagar é: R${:.2f}'.format((d*60) + (km*0.15)))
