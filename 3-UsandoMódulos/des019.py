from random import choice

print('Escolhendo um item da lista')

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
list = [n1, n2, n3, n4]
sort = choice(list)
print('O nome aluno escolhido foi {}'.format(sort))

fim = input('\nCurso de Python no YouTube, canal CURSO EM VIDEO.')