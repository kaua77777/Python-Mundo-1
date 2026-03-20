import math

x = float(input('Comprimento do cateto oposto: '))
y = float(input('Comprimento do cateto adjacente '))
z = math.sqrt(x**2 + y**2)

print (f' A hipotenusa é {z:.2f}')
