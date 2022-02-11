# Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome

nome_completo= input('Infome seu nome completo: ')
nome_completo = nome_completo.title()

if "Silva" in nome_completo:
    print('Esse pessoa possui "Silva" nome')
else:
    print('Esse pessoa não possui "Silva" nome')