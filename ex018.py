import math
n = float(input('Qual é o número? '))
n = math.radians(n)
print('O cosseno é {:.2f}'. format(math.cos(n)))
print('O seno é {:.2f}'.format(math.sin(n)))
print('A tangente é {:.2f}'.format(math.tan(n)))