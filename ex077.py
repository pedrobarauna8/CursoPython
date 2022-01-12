palavras = ('python', 'update', 'celular', 'coracao')
'aeiou' in palavras[0]
for c in palavras:
    print(f'\nNa palavra {c} temos ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
