from math import hypot
print('Calculando a hipotenusa')

co = float(input('Digita número do cateto oposto: '))
ca = float(input('Digita número do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

fim = input('\nCurso de Python no YouTube, canal CURSO EM VIDEO.')