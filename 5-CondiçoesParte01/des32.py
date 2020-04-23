print('\nAno Bissexto\n')

ano = int(input('Que ano você está ? '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Voce está em um ano Bissexto')
else:
    print('Voce não está em um ano Bissexto')

fim = input('\nCurso de Python no YouTube, canal CURSO EM VIDEO.')