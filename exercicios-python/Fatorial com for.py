x = int(input('Digite o número que deseja saber o fatorial: '))
f = 1
for c in range(1, (x + 1)):
    f *= c
print(f)