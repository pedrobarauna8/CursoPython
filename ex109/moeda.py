def metade(preco=0, formatar=False):
    res = preco * 0.50
    return res if formatar is False else moeda(preco)


def dobro(preco=0, formatar=False):
    res = preco * 2
    return res if formatar is False else moeda(preco)


def aumentar(preco=0, taxa=0, formatar=False):
    res = preco * ((taxa/100) + 1)
    return res if not formatar else moeda(preco)


def diminuir(preco=0, taxa=0, formatar=False):
    res = preco - (preco * (taxa/100))
    return res if not formatar else moeda(preco)


def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')