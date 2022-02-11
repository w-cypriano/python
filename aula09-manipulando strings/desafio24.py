# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

city = input('Informe o nome da cidade: ')
city = city.upper()
if city[:5] == 'SANTO':
    print('A cidade começa com SANTO')
else:
    print('A cidade não começa com SANTO')
