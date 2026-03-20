valor = float(input('O valor do produto é R$'))
desconto = 5
preco_final = valor - (valor * desconto / 100)
print (f'O valor com o desconto aplicado de 5% fica R${preco_final:.2f}')
