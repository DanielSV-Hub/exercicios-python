x = float(input('Digite o valor da mercadoria: '))
y = int(input('Digite o valor do desconto: '))
p = y / 100
xD = x - (x * p)
print('O novo valor da mercadoria após o desconto é de %.2f' % xD)
