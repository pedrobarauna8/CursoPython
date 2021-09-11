from random import randint
itens = ('1','2','3')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
if computador == 0 and jogador == 0:
    print('EMPATE!')
elif computador == 0 and jogador == 1:
    print('EU PERDI :(')
elif computador == 0 and jogador == 2:
    print('EU GANHEI!')
elif computador == 1 and jogador == 0:
    print('EU GANHEI')
elif computador == 1 and jogador == 1:
    print('EMPATE')
elif computador == 1 and jogador == 2:
    print('EU PERDI :(')
elif computador == 2 and jogador == 0:
    print('EU PERDI :(')
elif computador == 2 and jogador == 1:
    print('EU GANHEI!')
elif computador == 2 and jogador == 2:
    print('EMPATE!')
