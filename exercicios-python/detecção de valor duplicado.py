l = list()
while True:
    x = int(input('Digite o valor a ser adicionado: '))
    if x not in l:
        l.append(x)
        print('Valor adicionado com sucesso!')
    elif x in l:
        print('Valor duplicado, portanto não será adicionado.')
    resp = str(input('Deseja continuar [S/N]: '))
    if resp in 'nN':
        break
l.sort()
print(l)
print('Os valores adicionados foram:')
for c, v in enumerate(l):
    print(f'{v} na posição {c}')
