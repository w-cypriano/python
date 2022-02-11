# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

number = int(input('Digite o número desejado: '))

print('O dobro do número: {} O triplo: {} e raiz quadrada: {}'
.format(number*2, number*3, number**(1/2)))
#  number**(1/2) poder ser também number**0.5