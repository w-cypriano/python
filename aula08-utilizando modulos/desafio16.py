from math import trunc
#crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção inteira.

number_real = float(input('Digite um número real: '))
print('A porção inteira é: {}'.format(int(number_real))) # ou
print('A porção inteira é: {}'.format(trunc(number_real)))
