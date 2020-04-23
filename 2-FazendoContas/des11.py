print('Pintando Paredes')

larg = float(input('Lagura da parede '))
altu = float(input('Altura da parede '))
area = larg * altu
tinta = area / 2
print('Sua parede tem a dimensão de [{} x {}] e sua área é de [{}²]'.format(larg, altu, area))
print('Para pintar essa parede você precisará de [{}] de tinta'.format(tinta))

fim = input('\nCurso de Python no YouTube, canal CURSO EM VIDEO.')