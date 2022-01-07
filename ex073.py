brasileirao = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
               'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo',
               'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport',
               'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f'Os 5 primeiros são {brasileirao[0:5]}')
print(f'Os 4 últimos são {brasileirao[-4:]}')
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print(f'A Chapecoense está na {brasileirao.index("Chapecoense")+1}ª posição')