n = int(input('Digite um número para calcular seu Fatorial: '))
count = 0
f = 0
#for c in range (1, n):
#    if count == 1:
#        f = n * (n - 1)
#        count += 1
#        print(f, count)
#    else:
#        f *= (n - count)
#        count += 1
#print('O fatorial de {} é {}'.format(n, f))
while count != n:
    if count == 1:
        f = n * (n - 1)
        count += 1
        print(f, count)
    else:
        f *= (n - count)
        count += 1
print('O fatorial de {} é {}'.format(n, f))