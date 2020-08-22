x = int(input('Digite o número o qual deseja saber seu fatorial: '))
c = x
f = 1
while c > 0:
    f *= c
    c -= 1
print(f)