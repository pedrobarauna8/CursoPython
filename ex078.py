n = []
for c in range(0,5):
    n.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Você digitou os valores: {n}')
print(f'O maior valor digitado foi {max(n)}', end=' ')
for i, v in enumerate(n):
    if v == max(n):
        print(f'na posição {i}')
print(f'O menor valor digitado foi {min(n)}', end=' ')
for i, v in enumerate(n):
    if v == min(n):
        print(f'na posição {i}')
