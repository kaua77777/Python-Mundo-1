km = float(input('Quantos kilometros você percorreu com o carro? >> '))
dias = int(input('Você usou o carro durante quantos dias? >> '))
total1 = km * 0.15
total2 = dias * 60
total3 = total1 + total2 
print (f'Você tem quem pagar um total de R${total3} pelo uso do carro!')
