# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido.
import random
from unittest import result


list_alunos = []
while len(list_alunos) < 4:
    nome = input('digite o nomes dos alunos: ')
    list_alunos.append(nome)
resultado = random.choices(list_alunos)
print('Alunos: {}'.format(resultado[0]))