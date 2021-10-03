count = 1
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
while count != 10:
    print('{}'.format(n1 + (count - 1) * r), end=' → ')
    count += 1
print(end='FIM!!!')
