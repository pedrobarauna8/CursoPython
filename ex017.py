import math
c1 = float(input('Qual é a medida de um cateto? '))
c2 = float(input('Qual é a medida do outro cateto? '))
print('A hipotenusa é {:.2f}'.format(math.hypot(c1, c2)))