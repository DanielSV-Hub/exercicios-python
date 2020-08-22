# programa que pede horas, dias minutos e segundos e converte tudo para segundos
x = int(input('Digite a quantidade de dias: '))
y = int(input('Digite a quantidade de horas: '))
w = int(input('Digite a quantidade de minutos: '))
z = int(input('Digite a quantidade de segundos: '))
s1 = x * 24 * 60 * 60
s2 = y * 60 * 60
s3 = w * 60
total = s1 + s2 + s3 + z
print('O total de segundos foi %ds' % total)
