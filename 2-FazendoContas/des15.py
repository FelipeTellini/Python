print('Aluguel de Carro')

dia = float(input('Quantos dia o carro ficou alugaro ? '))
kmh = float(input('Quntos Km foi percorrido no carro ? '))
car = dia * 60
km  = kmh  * 0.15
total = (dia * 60) + (kmh * 0.15)
print(f'Valor por dias alugado R${car:.2f} Valor por Km percorido R${km:.2f}')
print(f'Total a pagar R${total:.2f}')

fim = input('\nCurso de Python no YouTube, canal CURSO EM VIDEO.')