from time import sleep


def contador(inicio, fim, passo):
    print(f'\nContagem de {inicio} até {fim} de {passo} em {passo}')
    if passo < 0:
        passo = passo * (-1)
    if passo == 0:
        passo = 1
    if fim > inicio:
        for c in range(inicio, fim + 1, passo):
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
    else:
        passo = -passo
        for c in range(inicio, fim - 1, passo):
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
    print()

# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)