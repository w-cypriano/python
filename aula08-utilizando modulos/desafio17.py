#faça um programa que leia o comprimento dos catete oposto e o comprimento do cateto adjacente 
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
cateto_oposto = int(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = int(input("Digite o comprimento do catete adjacente: "))

print('O valor de hipotenuza é: {:.2f}'.format(hypot(cateto_adjacente, cateto_oposto)))