print('\nAumento mútiplos\n')

salario = float(input('Qual o seu salário ? '))

if  salario  <= 1.200:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print('\nQuem ganhava \033[4;31mR${:.2f}\033[m passa a ganhar \033[4;32mR${:.2f}\033[m agora.'.format(salario, novo))


fim = input('\nCurso de Python no YouTube, canal CURSO EM VIDEO.')
