# O motorista que estiver acima de 80km será multado
x = int(input('Informe a velocidade do seu carro em km: '))
if x <= 80:
    print('Velocidade OK!')
if x > 80:
    y = x - 80
    z = y * 5
    float(z)
    print('VOCÊ ESTAVA EM ALTA VELOCIADE!!!')
    print('Para cada km acima de 80, será cobrado R$5. ')
    print('O valor da sua multa foi de R$%.2f' % z)
