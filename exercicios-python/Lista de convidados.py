l = list()
for x in range(0, 3):
    l.append(str(input('Digite o nome do convidado: ')))
c = 0
while c < 3:
    print(f'Olá {l[c]}, gostaria de jantar conosco?')
    c += 1
print('~' * 30)
f = l.pop(2)
print(f'Infelizmente o convidado(a) {f} não poderá comparecer.')
l.append(str(input('Digite o nome do novo convidado: ')))
print(f'O novo convidado é {l[2]}, estamos esperando.')
print(f'{l[0]} e {l[1]} o convite continua de pé.')
