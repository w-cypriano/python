# Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separamente.

nome= input('Informe o nome completo: ')
list_nome = nome.split()
print('o primeiro nome é: {}, e o último nome: {}'.format(list_nome[0], list_nome[-1]))