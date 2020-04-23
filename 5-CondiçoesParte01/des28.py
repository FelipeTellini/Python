from random import randint
computador = randint(0, 10) #Faz o computador pensar...

cor = {'limpa \033[m','roxa \033[1;35m','amarelo \033[1;33m',
'verde \033[32m','vermelho \033[31m','azul \033[34m'}

print('\033[1;35m=\033[m'*10)
print('\033[34m Vou pensar em um número de 0 a 10 tente advinhar...')
print('\033[1;35m=\033[m'*10)

#O jogador tenta advinhar..

jogador = int(input('\033[1;33m Em que número eu pensei \033[m ? '))

if jogador == computador:
    print('\033[4;32m Parabéns voce conseguiu me vencer !!!')
else:
    print('\n\033[36m GANHEI! Eu pensei no número \033[32m{}\033[m \033[36m e não no número \033[m \033[31m{}\033[m'.format(computador, jogador))
    

fim = input('\nCurso de Python no YouTube, canal CURSO EM VIDEO.')