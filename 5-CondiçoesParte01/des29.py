print('\n\033[1;31m Radar eletronico\n')

vel = float(input('\033[1;35m Qual a velocidade do carro: '))
mul = (vel-80)*7
if vel <=80:
    print('\n\033[1;37;40m O carro está no limete da velocidade, Dirija com segurança!')
else:
    print('\n\033[1;33;40m O carro levou multa exesso de velocidade.\nTotal a pagar R${:.2f}'.format(mul))

fim = input('\n\033[32mCurso de Python no YouTube, canal CURSO EM VIDEO.')