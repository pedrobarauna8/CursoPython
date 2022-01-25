from random import randint


def sorteia():
    for c in range(0, 5):
        lista.append(randint(0, 10))
    print(f'Os números sorteados foram: {lista}')


def somapar():
    soma = 0
    for c in range(0, len(lista)):
        if lista[c] % 2 == 0:
            soma = soma + lista[c]
    print(f'A soma dos valores pares é: {soma}')

# Programa Principal
lista = []
sorteia()
somapar()