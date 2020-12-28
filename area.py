import time

#calcular área de um circulo

#fórmula: a = π.r²

pi = 3.14

converter = input('Centímetros ou metros? ')
time.sleep(0.5)
raio = float(input('Digite o valor do raio: '))
time.sleep(0.5)

#converter de centímetros para metros

if converter == 'metros':
    area = pi*(raio**2)
    time.sleep(0.5)
    resultado1 = print(f'O valor da área do circulo é: {area} metros')

if converter == 'centímetros':
    area2 = pi*(raio**2)
    time.sleep(0.5)
    resultado1 = print(f'O valor da área do circulo é: {area2} centímetros')