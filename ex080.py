lista = list()
count = 0
for c in range(0,6):
    n = int(input('Digite um valor: '))
    if count == 0:
        count += 1
        lista.append(n)
        print('Número adicionado na última posição')
    #if n > lista[0]:
    #    lista.insert(n)
print(lista)
