print('\nCusto da viagem\n')

kmh= int(input('Qual a distancia de sua viagem ? '))

km1 = kmh * 0.50
km2 = kmh * 0.45

if  kmh <= 200:
    print('\nSua viagem vai custar R${:.2f}'.format(km1))
else:
    print('\nSua viagem vai custar R${:.2f}'.format(km2))

    fim = input('\nCurso de Python no YouTube, canal CURSO EM VIDEO.')