print('Calculando Descontos')

produto = float(input('Qual é o preço do produto ? R$'))
desconto = produto - (produto * 5) /100
print('O produto que custava R${:.2f} '.format(produto),end='')
print('na promoção de 5% vai custar R${:.2f}.'.format(desconto))

fim = input('\nCurso de Python no YouTube, canal CURSO EM VIDEO.')