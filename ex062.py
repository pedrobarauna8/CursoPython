a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
n = 10
i = 0
while(n!=0):
    i = 0
    while (i < n):
        print(a1, end=' → ')
        a1 = a1 + r
        i = i + 1
    print('PAUSA')
    n = int(input('Qunatos termos vc quer mostrar a mais?'))
