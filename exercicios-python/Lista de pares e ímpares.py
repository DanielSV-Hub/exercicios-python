num = [[], []]
for cont in range(0, 7):
    n = (int(input(f'Digite o valor da posição {cont + 1}: ')))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print('~' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares foram: {num[0]}')
print(f'Os valores ímpares foram: {num[1]}')