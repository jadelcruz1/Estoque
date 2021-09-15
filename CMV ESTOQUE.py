#codigo criado para calculo de cmv ( custo mercadoria vendida) em Reais R$

EstoqueInicial = float(input(' Insira o estoque inicial da fabrica:')) #valores em float pois se trata de dinheiro.
Compras = float(input('Insira os valores de compras:'))
Vendas = float(input('Insira o valor de venda:'))

CMV = EstoqueInicial + Compras - Vendas

print(CMV)