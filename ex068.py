from random import randint
count = 0
while True:
    nu = int(input('Digite um número de 0 a 10: '))
    npc = randint(0, 10)
    u = input('ímpar ou Par? [I/P]: ')
    n = nu + npc
    print(f'Você jogou {nu} e o computador {npc}. O total é {n}')
    if n % 2 == 0 and u == 'P':
        print('O Usuário venceu.')
        count += 1
    elif n % 2 != 0 and u == 'I':
        print('O Usuário venceu.')
        count += 1
    else:
        break
print(f'O usuário venceu {count} vezes seguidas.')
