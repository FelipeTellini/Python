print('\nPrimeira e última ocorrência de uma strig\n')

nome = str(input('Digita uma frase: ')).upper().strip()
print('A letra  A  aparece {} vez na frase'.format(nome.count('A')))
print('A primeira letra  A  apareceu na posiçao {}'.format(nome.find('A')+1))
print('A ultima letra  A  apareceu na posiçao {}'.format(nome.rfind('A')+1))

fim = input('\nCurso de Python no YouTube, canal CURSO EM VIDEO.')