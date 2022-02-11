# Faça um programa que eleia um noumero de 0 a 9999 e mostre
# na tela cada um dos digitos separados.
# Ex: entrada: 1834 saida unid:4 dezenas 3 ... 

number = input('Digite o número desejado(somente 4 digito): ')

if len(number) > 4:
    number = input('Digite somente 4 digito: ')
print('decomposição: unidade: {}, dezena: {}, centena: {}, milhar: {},'
.format(number[3], number[2], number[1], number[0]))