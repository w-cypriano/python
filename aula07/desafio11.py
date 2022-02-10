# Faça um programa que leia a largura e altura de uma parede,
# calcule a sua área e a quantidade de tinta necessaria para pintá-la.
# Sabendo que cada litro de tinta pinta uma área de 2m².

altura = int(input('informe a altura: '))
largura = int(input('informe a largura: '))
area_por_litro = 2

print('São necessarios: {} litros para pintar toda área'.format(altura * largura/2))