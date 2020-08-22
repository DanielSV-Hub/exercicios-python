usu = str(input('Digite seu nome de usuário: ')).upper()  # pede o nome do usuário no formato str
sen = str(input('Digite a senha: ')).upper()  # pede a senha do usuário no formato str
sen2 = sen  # guarda o valor da variável sen
while sen2 == usu:  # enquanto a senha for igual ao nome do usuário o program irá se repetir
    print('Erro! Seu nome de usuário não pode ser igual a senha. Tente novamente.')
    sen2 = str(input('Digite a senha: ')).upper()
if sen2 != usu:  # se a senha for diferente do nome do usuário, o cadastro é realizado
    print('Cadastro feito com sucesso!')