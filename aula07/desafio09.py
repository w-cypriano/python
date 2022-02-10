# Faça um programa que leia um número inteiro qualquer 
# e mostre na tela a sua tabuada

number = int(input('Digite o número: '))
tab = 0
while tab <= 10:
    print('{}+{} = {}'.format(number, tab, number + tab))
    tab +=1