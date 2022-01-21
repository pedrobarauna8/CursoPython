from random import randint
list = []
jogos = []
qjogos = int(input('Quantos jogos serão gerados? '))
for j in range(0, qjogos):
    for c in range(0,6):
        list.append(randint(0,60))
    list.sort()
    jogos.append(list[:])
    list.clear()
    print(f'\nJogo {j+1}: {jogos[j]}', end='')
