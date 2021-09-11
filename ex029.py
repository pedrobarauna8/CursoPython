velocidade = float(input('Qual é a velocidade? '))
if velocidade < 80:
    print('Acelera esse carro, limites foram feitos para serem ultrapassados')
else:
    diferenca = velocidade - 80
    print('Tá certo, tem que acelerar mesmo, mas vai tomar multinha de {:.2f} R$ '.format(diferenca*7))
