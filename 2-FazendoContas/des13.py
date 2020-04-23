print('Reajuste Salárial.')

salario = float(input('Qual é o salário do funcionário: R$'))
novo = salario + (salario * 15) /100
print(f'Um funcionário que ganhava R${salario:.2f}, ',end='')
print(f'com 15% de almento, passa receber R${novo:.2f}')

fim = input('\nCurso de Python no YouTube, canal CURSO EM VIDEO.')