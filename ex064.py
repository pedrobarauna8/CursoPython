n = 0
n1 = 0
count = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    count += 1
    n1 += n
print('Você digitou {} números e a soma foi {}'.format(count, n1-999))
