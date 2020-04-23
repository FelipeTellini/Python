from random import shuffle

print('Sorteando uma ordem de lista')

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
list = [n1, n2, n3, n4]
shuffle(list)
print('A ordem de serviços será:')
print(list)

fim = input('\nCurso de Python no YouTube, canal CURSO EM VIDEO.')