# O mesmo professor do desafio anterior que sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle


list_alunos = []
ordem = ""
while len(list_alunos) <4:
    nome = input('digite o nome do aluno: ')
    list_alunos.append(nome)

shuffle(list_alunos) # metodo faz o embaralhamento da lista.

print('A ordem é: {}'.format(list_alunos))