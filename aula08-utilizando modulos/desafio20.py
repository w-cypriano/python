# O mesmo professor do desafio anterior que sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random 


list_alunos = []
ordem = ""
while len(list_alunos) <4:
    nome = input('digite o nome do aluno: ')
    list_alunos.append(nome)

for x in range(len(list_alunos)):
    resultado = random.choice(list_alunos)
    ordem = ordem + resultado + ', '
print('A ordem é: {}'.format(ordem))