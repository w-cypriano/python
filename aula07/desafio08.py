#Escreva um programa que leia um valor em metros 
# e o exiba convertido em centímetros e milímetros.

number_mts = int(input('Digite o valor em metros: '))

print('A valor em centimetros é: {}cm, e em milímetros é: {}mm'.format(number_mts*100, number_mts *1000))