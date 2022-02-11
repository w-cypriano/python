#crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras Maísculas.
# O nome com todas as letras minusculas.
# Quantas letras ao todo(sem considerar espaços)
# Quantas letras tem o primeiro no nome.

nome_completo = input('Digite seu nome completo: ')

print('Seu nome em letras maiusculas: {}'.format(nome_completo.upper()))
print('Seu nome em letras minusculas: {}'. format(nome_completo.lower()))
print('Quantidade de letras no seu nome(sem espaço): {}'.format(len(nome_completo.replace(" ", ""))))
print('Quantidade de letras tem o primeiro nome: {}'.format(len(nome_completo.split()[0])))