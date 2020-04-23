print('\nAnalizando Triângulo\n')

r1 = float(input('Primeiro Seguimento '))
r2 = float(input('Segundo Seguimento '))
r3 = float(input('Terceiro Seguimento '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;32m Os seguimentos acima podem formar um triângulo\033[m')
else:
    print('\033[1;31m Os seguimentos acima não podem formar um triângulo\033[m')

    fim = input('\nCurso de Python no YouTube, canal CURSO EM VIDEO.')