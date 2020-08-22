x = 1
soma = 0
cont = 0
while x != 0:
    cont += 1
    x = int(input('Digite o valor de x: '))
    soma += x
print('Você digitou %d números a soma entre eles é %d e sua média é %d' % (cont - 1, soma, soma / (cont - 1)))