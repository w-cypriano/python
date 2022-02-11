# faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = input('Digite a frase: ')
frase = frase.upper()
print('A letra "A" aparece: {} vezes'.format(frase.count('A')))
print('A primeira letra "A" aparece na posição: {}'.format(frase.find('A')))
print('A última letra "A" aparece na posição: {}'.format(frase.rfind('A'))) 
# rfind  inicia a busca da direita pra esquerda pegando sempre o primeiro.