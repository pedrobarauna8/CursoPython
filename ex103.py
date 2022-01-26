def ficha(nome=0, gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


nome = str(input('Nome do jogador: '))
gols = int(input('Número de gols: '))
ficha(nome,gols)