n = int(input('Digite um número: '))
escolha = int(input('Escolha uma das bases para a conversão:'
      '\n[ 1 ] converter para BINÁRIO' 
      '\n[ 2 ] converter para OCTAL'
      '\n[ 3 ] converter para HEXADECIMAL'
      '\nSua opção: '))
if escolha == 1:
    binario = bin(n)[2:]
    print('{} convertido para BINÁRIO é {}'.format(n, binario))
elif escolha == 2:
    octal = oct(n)[2:]
    print('{} convertido para OCTAL é {}'.format(n, octal))
elif escolha == 3:
    hexa = hex(n)[2:]
    print('{} convertido para HEXADECIMAL é {}'.format(n, hexa))
else:
    print('OPÇÃO INVÁLIDA. Tente novamente')