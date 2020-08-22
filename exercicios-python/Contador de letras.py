x = input('Digite sua mensagem: ')
cont = 0
for c in x:
    cont += 1
if cont > 6:
    print(f'Mensagem inválida, pois possui {cont} caracteres')
else:
    print('Mensagem OK!')