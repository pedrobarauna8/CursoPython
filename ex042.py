a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Forma um triângulo ', end = '')
    if a == b == c:
            print('equilátero')
    elif a == b or a == c or b == c:
            print('isósceles')
    else:
        print('escaleno')
else:
    print('Não forma um triângulo')
