matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = somat = maior = 0
for c in range(0, 3):
    for l in range(0, 3):
        matriz[c][l] = int(input(f'Digite um valor para [{c}, {l}]: '))
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[c][l]:^5}]', end='')
    print()
print('-='*30)
for c in range(len(matriz[c])):
    for l in range(len(matriz[l])):
        if matriz[c][l] % 2 == 0:
            somap += matriz[c][l]
print(f'A soma dos números pares é {somap}')
for c in range(0,3):
    somat += matriz[c][2]
print(f'A soma dos números da terceira coluna é {somat}')
for c in range(0,3):
    if matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior número da segundo linha é {maior}')