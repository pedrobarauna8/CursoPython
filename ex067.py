while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    count = 0
    for c in range(1,11):
        print(f'{n} X {c} = {n * c}')
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')
