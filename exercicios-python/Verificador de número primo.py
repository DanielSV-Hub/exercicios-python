# Verifica se um número é primo ou não
x = int(input('Digite o número que deseja verificar: '))
tot = 0
for c in range(1, x+1):
    if x % c == 0:
        print('\033[36m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print(c, end=' ')
if tot == 2:
    print('\nNúmero primo \033[m')
else:
    print('\nNúmero não primo \033[m')