def ficha(nome='', gol=0):
    if nome == '':
        nome = '<desconhecido>'
    if not gol.isdigit():
        gol = 0
    print(f'O jogador {nome} fez {gol} gols no campeonato')


nome = str(input('Nome do jogador: ')).strip().title()
gols = input('Número de gols: ').strip()
ficha(nome,gols)