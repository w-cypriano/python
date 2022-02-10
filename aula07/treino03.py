# definir a quantidade de casa decimais que serão exibidas
number1 = int(input('Digite um número: '))
number2 = int(input('Digite outro número: '))

print('O resultado da divisão é: {}'.format(number1/number2), end=' ')
print('O resultdo da divisão é: {:.3f}'.format(number1/number2))
# {:.3f} indica que será exibido apenas 3 casas decimais o 'f' significa float flutuante,
# ou seja 3 casas flutuantes
# O comando 'end=' ' no final do print impede a quebra automatica do print, use um espaço dentro
# das aspas pra conseguir um espaço entre os dois print´s