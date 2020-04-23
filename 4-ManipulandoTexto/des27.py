print('\n Primeiro e último nome de uma pessoa \n')

nome1 = str(input('Digite seu nome completo: ')).strip()
nome2 = nome1.split()
print('O primeiro nome é {}'.format(nome2[0]))
print('O seu ultimo nome é {}'.format ( nome2 [ len ( nome2 ) -1 ] ))

fim = input('\nCurso de Python no YouTube, canal CURSO EM VIDEO.')