e = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while not e == 5:
    print('[ 1 ] somar\n'
          '[ 2 ] multiplicar\n'
          '[ 3 ] maior\n'
          '[ 4 ] novos números\n'
          '[ 5 ] sair do programa\n')
    e = int(input('Qual é a sua opção? '))
    if e == 1:
        print('A soma de {} e {} é {}'.format(n1, n2, (n1 + n2)))
    elif e == 2:
        print('A multiplicação de {} e {} é {}'.format(n1, n2, (n1 * n2)))
    elif e == 3:
        if n1 > n2:
            print('O número {} é maior que {}'.format(n1, n2))
        else:
            print('O número {} é maior que {}'.format(n2, n1))
    elif e == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        print('Opção Inválida. Tente Novamente')