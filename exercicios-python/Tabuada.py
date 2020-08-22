tabuada = 1
print('~' * 30)
print('Tabuada')
print('~' * 30)
while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print('%d X %d = %d' % (tabuada, numero, tabuada * numero))
        numero += 1
    print('~' * 30)
    tabuada += 1