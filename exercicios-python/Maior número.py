x = int(input('Digite um número: '))
y = int(input('Digite um número: '))
z = int(input('Digite um número: '))
if x > y and x > z:
    print('O maior valor foi %d' % x)
elif y > x and y > z:
    print('O maior valor foi %d' % y)
elif z > x and z > y:
    print('O maior valor foi %d' % z)
