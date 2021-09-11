from datetime import date
ano = int(input('Insira um ano: Coloque 0 para analisar o ano atual'))
if ano == 0:
    ano = date.today().year
if ano%100 != 0:
    resultado = ano%4
    if resultado == 0:
        print('O ano {} é bissexto! '.format(ano))
    else:
        print('O ano {} não é bissexto. '.format(ano))
else:
    resultado1 = ano%400
    if resultado1 == 0:
        print('O ano {} é bissexto! '.format(ano))
    else:
        print('O ano {} não é bissexto! '.format(ano))
