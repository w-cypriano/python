nome = input('qual seu nome: ')

print('seja bem-vindo {}!'.format(nome))
#print('seja bem-vindo {:20}!'.format(nome)) # repare que foi colocar 20 espaços depois de nome
#print('seja bem-vindo {:>20}!'.format(nome)) # coloque 20 espaço no nome e alinhou a direita.
print('seja bem-vindo {:<20}!'.format(nome)) # coloque 20 espaço no nome e alinhou a esquerda.
print('seja bem-vindo {:^20}!'.format(nome)) #  coloque 20 espaço no nome e centralizou.
print('seja bem-vindo {:=^20}!'.format(nome)) #  coloque 20 espaço no nome e centralizou
# e ainda colocou os sinais de =. ideal pra montar tela, podemos colocar qualquer ao em ves de =