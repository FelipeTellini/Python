print('\nSeparando digitos de um número\n')

num = int(input('´Digita um número: '))
print('\nAnalizando o número digitado ... ')
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade {}\nDezena {}\nCentena {}\nMilhar {}'.format(u, d, c, m))

fim = input('\nCurso de Python no YouTube, canal CURSO EM VIDEO.')