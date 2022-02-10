#Faça um programa que leia um ângulo qualquer 
# e mostre na tela valor de seno, conseno e tangente desse ângulo.
from math import cos, sin, tan


angulo = int(input('Digite o valor ângulo: '))
print('O valores são: seno: {}, conseno: {}, tangente: {}'.format(cos(angulo), sin(angulo), tan(angulo)))