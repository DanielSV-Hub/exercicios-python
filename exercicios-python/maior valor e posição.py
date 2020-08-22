l = list()
for x in range(0, 5):
    l.append(int(input(f'Digite o valor da posição {x + 1}: ')))
for c, v in enumerate(l):
    if v == max(l):
        print(f'O maior valor é {max(l)} na posição {c + 1}...')
    elif v == min(l):
        print(f'O menor valor é {min(l)} na posição {c + 1}')