ne = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
      'seis', 'sete', 'oito', 'nove', 'dez',
      'onze', 'doze', 'treze', 'quatorze', 'quinze',
      'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente Novamente. ', end='')
    print(f'Você digitou o número {ne[n]}')
    c = ' '
    while c not in 'SN':
        c = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if c == 'N':
        break