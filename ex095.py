dict = {}
lista = []
jogadores = list()
while True:
    total = 0
    dict['Nome do jogador'] = str(input('Nome do jogador: '))
    dict['Partidas'] = int(input(f'Quantas partidas {dict["Nome do jogador"]} jogou? '))
    for c in range(1, dict['Partidas']+1):
        gols = (int(input(f'Gols na partida {c}: ')))
        lista.append(gols)
        total += gols
    dict['Gols'] = lista[:]
    dict['Total de gols'] = total
    jogadores.append(dict.copy())
    del dict['Nome do jogador']
    del dict['Partidas']
    del dict['Gols']
    del dict['Total de gols']
    lista.clear()
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
for c in range(0, len(jogadores)):
    print(c+1, jogadores[c]['Nome do jogador'], jogadores[c]['Gols'], jogadores[c]['Total de gols'])
while True:
    j = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if j != 999:
        for c in range(0, len(jogadores[j-1]["Gols"])):
            print(f'No jogo {c+1} fez {jogadores[j-1]["Gols"][c]} gols.')
    else:
        break