from math import sin, cos, tan, radians

print('Seno - Cosseno - Tangente')

ang = float(input('Digite o ângulo: '))
sen = sin(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang,sen))

cos = cos(radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))

tan = tan(radians(ang))
print('O ângulo de {} ten a TANGENTE de {:.2f}'.format(ang, tan))

fim = input('\nCurso de Python no YouTube, canal CURSO EM VIDEO.')