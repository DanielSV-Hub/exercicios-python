x = 0
c = 0
while x != 999:
    x = int(input('Digite o valor de x: '))
    if x != 999:
        c += x
    else:
        break
print(f'A soma dos valores {c}')