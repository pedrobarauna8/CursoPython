distancia = float(input('Qual é a distância? '))
if distancia <= 200:
    print('O preço será de R$ {:.2f}'.format(distancia*0.50))
else:
    print('O preço será de R$ {:.2f}'.format(distancia*0.45))
