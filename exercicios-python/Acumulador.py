n = 0
soma = 0
base = soma
while n < 10:
    x = int(input('Digite o valor de x: '))
    base = soma + x
    n += 1
    print('A soma de %d com %d é %d' % (soma, x, base))
    soma = base