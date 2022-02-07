def leiaInt(n=0):
    n = input('Digite um número: ')
    while not n.isnumeric():
        print('\033[0;31mDigite um número inteiro válido.\033[m')
        n = input('Digite um número: ')
    return n


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')