l = [[], [], [], [], [], [], [], [], []]
c = 0
while c < 9:
    n = int(input('Digite um valor: '))
    l[c].append(n)
    c += 1
print(f'{l[0]} {l[1]} {l[2]} '
      f'\n{l[3]} {l[4]} {l[5]}'
      f'\n{l[6]} {l[7]} {l[8]}')