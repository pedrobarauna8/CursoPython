maior = nome = count = count1 = s = 0
while True:
    produto = input('Nome do Produto: ')
    preco = int(input('Preço: R$ '))
    s += preco
    count1 += 1
    if preco > 1000:
        count += 1
    if count1 == 1:
        nome = produto
        maior = preco
    else:
        if preco < maior:
            maior = preco
            nome = produto
    c = input('Quer continuar? [S/N] ')
    if c == 'N':
        break
print(f'O total da compra foi de R$ {s:.2f}')
print(f'Temos {count} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {nome} que custou R$ {maior:.2f}')
