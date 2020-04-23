print('\nAnalizador de texto\n')

nome = str(input('Digita seu nome completo: ')).strip()
print('\nAnalizando seu nome...')
print('Seu nome completo em tudo MAIÚSCULAS -> {}'.format(nome.upper()))
print('Seu nome completo em tudo minúsculas -> {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro tem {} letras'.format(nome.find(' ')))
sepa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(sepa[0], len(sepa[0])))

fim = input('\nCurso de Python no YouTube, canal CURSO EM VIDEO.')