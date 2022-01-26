def votar(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    if 18 > idade >= 16 or idade >= 65:
        print(f'Com {idade}: VOTO OPCIONAL.')
    elif 15 >= idade:
        print(f'Com {idade}: VOTO NÃO PERMITIDO')
    else:
        print(f'Com {idade}: VOTO OBRIGATÓRIO')


ano = votar(int(input('Ano de nascimento: ')))