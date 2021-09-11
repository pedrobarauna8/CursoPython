n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2
print('Considerando as notas {:.2f} e {:.2f}, a média do aluno é {:.2f}'.format(n1, n2, media))
if media >= 7.0:
    print('APROVADO!')
elif media >= 5.0:
    print('RECUPERAÇÃO!')
else:
    print('REPROVADO!')
