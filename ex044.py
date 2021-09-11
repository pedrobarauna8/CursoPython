total = float(input('Preço das compras: R$ '))
opcao = int(input('FORMAS DE PAGAMENTO \n'
    '\n[ 1 ] à vista dinheiro/cheque'
    '\n[ 2 ] à vista cartão'
    '\n[ 3 ] 2x no cartão'
    '\n[ 4 ] 3x ou mais no cartão'
    '\nQual é a opção? '))
if opcao == 1:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(total, (total-(total*0.10))))
elif opcao == 2:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(total, (total-(total*0.05))))
elif opcao == 3:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(total, (total)))
elif opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final. Parcelada em {}x de R$ {} COM JUROS'.format(total, (total*1.20), parcela, ((total*1.20)/parcela)))
