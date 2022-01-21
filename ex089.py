lista = []
aluno = []
cont = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))
    cont += 1
    aluno.append(lista[:])
    lista.clear()
    r = str(input('Quer continuar? [S/N] '))
    if r not in 'Ss':
        break
for c in range(0, cont):
    print(c, aluno[c][0], (aluno[c][1]+aluno[c][2])/2)
while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        break
    print(f'As notas de {aluno[n][0]} são {aluno[n][1], aluno[n][2]}')
