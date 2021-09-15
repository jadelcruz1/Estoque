#codigo criado para calculo de cmv ( custo mercadoria vendida) em Reais R$
#versao com repeticao e contador de estoque = mais de uma compra
EstoqueInicial = float(input(' Insira o estoque inicial da fabrica:')) #valores em float pois se trata de dinheiro.
Compras = float(input('Insira os valores de compras:'))
Vendas = float(input('Insira o valor de venda:'))

CMV = (EstoqueInicial + Compras - Vendas)

#media_do_CMV = CMV/qtde_de_lancamentos - melhorar esse codigo para que me informe a media do cmv conforme a quantidade de lancamentos

if (CMV > 0):
    print(CMV)

else:
    print('Verificar possiveis omissões de notas fiscais')




