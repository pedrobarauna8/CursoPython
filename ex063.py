count = 3
t1 = 0
t2 = 1
n = int(input('Quantos termos você quer mostar? '))
print('{} → {}'.format(t1, t2), end='')
while count <= n:
    t3 = t1 + t2
    print('→ {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
print('FIM!')