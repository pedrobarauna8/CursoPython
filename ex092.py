from datetime import datetime
dict = {}
dict['Nome'] = str(input('Nome: '))
dict['Idade'] = int(input('Ano de Nascimento: '))
dict['Carteira de Trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))
if dict['Carteira de Trabalho'] != 0:
    dict['Ano de Contratação'] = int(input('Ano de contratação: '))
    dict['Salário'] = float(input('Salário: R$ '))
    dict['Aposentadoria'] = (dict['Ano de Contratação'] + 35) - dict['Idade']
    dict['Idade'] = datetime.now().year - dict['Idade']
for k, v in dict.items():
    print(f'{k}: {v}')
