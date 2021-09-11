n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
n10 = n1 + (10 - 1) * r
for c in range(n1+1, n10 + r, r):
    print('{}'.format(c-1), end=' → ')
print(end='FIM!!!')
