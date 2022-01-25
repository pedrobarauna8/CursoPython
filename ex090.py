notas = {}
notas['nome'] = str(input('Nome: '))
notas['media'] = float(input(f'Média de {notas["nome"]}: '))
if notas['media'] >= 6:
    notas['situacao'] = 'Aprovado'
else:
    notas['sitacao'] = 'Reprovado'
print(f'Nome: {notas["nome"]} \nMédia: {notas["media"]} \nSituação: {notas["situacao"]}')