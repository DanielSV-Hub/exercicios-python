salario = float(input('Digite seu salário: '))
base = salario
imposto = 0
if base > 3000:
    imposto += ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto += ((base - 1000) * 0.20)
print('Salário: R$%.2f / Imposto a ser pago: R$%.2f' % (salario, imposto))
