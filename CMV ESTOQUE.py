#codigo criado para calculo de cmv ( custo mercadoria vendida) em Reais R$
#versao com repeticao e contador de estoque = mais de uma compra


EstoqueInicial = float(input(' Insira o estoque inicial da fabrica:')) #valores em float pois se trata de dinheiro.
Compras = float(input('Insira os valores de compras:'))
Vendas = float(input('Insira o valor de venda:'))

CMV = (EstoqueInicial + Compras - Vendas)

if (CMV > 0):
    print(CMV)

else:
    print('Verificar possiveis omissões de notas fiscais')




