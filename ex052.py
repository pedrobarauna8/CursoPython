count = 0
n1 = int(input('Digite um número: '))
for c in range(1, n1+1):
    if n1 % c == 0:
        count += 1
if count <= 2:
    print('É primo!')
else:
    print('Não é primo!')
