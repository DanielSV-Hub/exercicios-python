x = float(input('Digite seu salário atual: '))
y = int(input('Digite a porcentagem do aumento: '))
p = y / 100
sA = x + (x * p)
print('Seu salário após o aumento é de R$ %.2f' % sA)