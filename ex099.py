def maior(*n):
    if n != ():
        print(n)
        print(f'Foram informados {len(n)} números')
        print(f'O maior número informado foi {max(n)}')
    else:
        print('Foram informados 0 números.\nO maior valor informado foi 0')


# Programa Principal
maior(2, 5, 8, 9, 4, 3)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()