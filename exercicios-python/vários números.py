l = list()
while True:
    l.append(int(input('Digite um valor: ')))
    res = str(input('Deseja continuar [S/N]?')).upper()
    if res == 'N':
        break
print(f'A lista foi {l}')
print(f'Você digitou {len(l)} elementos')
l.sort()
print(f'A lista em ordem fica: {l}')
l.reverse()
print(f'A lista em ordem decrescente é: {l}')
if 5 in l:
    print('O número cinco está na lista')
else:
    print('O número não está na lista')
