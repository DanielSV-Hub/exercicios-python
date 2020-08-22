l = list()
z = list()
for x in range(0, 2):
    n = input('Digite o elemento a ser adicionado: ')
    l.append(n)
print(f'Os elementos adicionados foram {l}')
for y in range(0, 2):
    u = input('Digite o elemento a ser adicionado: ')
    z.append(u)
print(f'Os elementos adicionados foram {z}')
w = l + z
print(f'A junção dos elementos é {w}')



