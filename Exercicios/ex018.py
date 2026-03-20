import math

angulo = int(input('Digite o angulo: '))

radianos = math.radians(angulo)

seno = math.sin(radianos)
cos = math.cos(radianos)
tan = math.tan(radianos)

print(f'O angulo de {angulo} tem o Seno de {seno:.2f}')

print(f'O angulo de {angulo} tem o Cosseno de {cos:.2f}')

print(f'O angulo de {angulo} tem a Tangente de {tan:.2f}')
