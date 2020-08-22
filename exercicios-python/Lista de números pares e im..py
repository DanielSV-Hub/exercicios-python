l = list()
p = list()
i = list()
while True:
    n = int(input('Digite um valor: '))
    l.append(n)
    if n % 2 == 0:
        p.append(n)
    elif n % 2 != 0:
        i.append(n)
    resp = str(input('Deseja continuar [S/N]: '))
    if resp in 'Nn':
        break
print('~' * 30)
print(f'A lista digitada foi {l}')
print(f'A lista de números pares é {p}')
print(f'A lista de números ímpares é {i}')