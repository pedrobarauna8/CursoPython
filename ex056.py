soma_idade = 0
cont = 0
maior_idade = 0
mais_velho = 0
mulheres = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    soma_idade += idade
    cont += 1
    if c == 1 and sexo == 'M':
        maior_idade = idade
        mais_velho = nome
    elif c != 1 and sexo == 'M':
        if idade > maior_idade:
            maior_idade = idade
            mais_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1
print('A média de idade do grupo é de {} anos'.format(soma_idade/cont))
print('O homem mais velho tem {} anos e se chama {} '.format(maior_idade, mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres))
