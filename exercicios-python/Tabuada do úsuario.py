x = int(input('Escreva um número interio o qual deseja saber sua tabuada: '))
while True:
    print('~' * 40)
    y = int(input('Opções: '
                  '\nAdição[1]'
                  '\nSubtração[2]'
                  '\nMultiplicação[3]'
                  '\nDivisão[4]'
                  '\nSair[5]'
                  '\nEscolha: '))
    if y == 1:
        print('-' * 30)
        print('Tabuada da adição')
        print('-' * 30)
        num = 1
        while num <= 10:
            soma = x + num
            print(f'{x} + {num} = {soma}')
            num += 1
    if y == 2:
        print('-' * 30)
        print('Tabuada da subtração')
        print('-' * 30)
        num = 1
        while num <= 10:
            sub = x - num
            print(f'{x} - {num} = {sub}')
            num += 1
    if y == 3:
        print('-' * 30)
        print('Tabuada da multiplicação')
        print('-' * 30)
        num = 1
        while num <= 10:
            mult = x * num
            print(f'{x} * {num} = {mult}')
            num += 1
    if y == 4:
        print('-' * 30)
        print('Tabuada da divisão')
        print('-' * 30)
        num = 1
        while num <= 10:
            div = x / num
            print(f'{x} / {num} = {div}')
            num += 1
    if y == 5:
        break