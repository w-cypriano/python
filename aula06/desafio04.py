#Faça um programa que leia algo pela teclado 
# e mostre na tela o seu tipo primitivo e todas informações possiveis sobre  ele

something = input("Digite algo: ")
print(type(something))
print('Recebeu um alfanumerico?', something.isalnum())
print('Recebeu um Decimal?', something.isdecimal())
print('Recebeu um digito?', something.isdigit())
print('Recebeu um numero?', something.isnumeric())
print('Recebeu algo que pode ser printado', something.isprintable())