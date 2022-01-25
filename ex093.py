dict = {}
lista = []
total = 0
dict['Nome do jogador'] = str(input('Nome do jogador: '))
dict['Partidas'] = int(input(f'Quantas partidas {dict["Nome do jogador"]} jogou? '))
for c in range(1, dict['Partidas']+1):
    gols = (int(input(f'Gols na partida {c}: ')))
    lista.append(gols)
    total += gols
dict['Gols'] = lista[:]
dict['Total de gols'] = total
for k, v in dict.items():
    print(f'{k}: {v}')
print('-='*20)
print(f'O jogador {dict["Nome do jogador"]} jogou {dict["Partidas"]} jogos.')
for c in range(0, dict['Partidas']):
    print(f'Na Partida {c+1}, fez {dict["Gols"][c]} gols.')
print(f'Foi um total de {dict["Total de gols"]} gols. E uma média de {(dict["Total de gols"]/dict["Partidas"]):.2f} gols por jogo')