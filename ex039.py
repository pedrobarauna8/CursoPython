from datetime import date
atual = date.today().year
ano = int(input('Qual ano você nasceu? '))
print('Quem nasceu em {} tem {} em {}'.format(ano, (atual-ano), atual))
if (2021-ano) < 18:
    print('Você ainda terá que se alistar')
    print('Faltam {} anos para seu alistamento que será em {}'.format((atual-ano+18), (ano+18)))
elif (2021-ano) > 18:
    print('Você já alistou')
    print('Fazem {} anos que você se alistou, que foi em {}'.format((atual-ano-18), (ano+18)))
elif (2021-ano) == 18:
    print('Você terá que se alistar esse ano')

