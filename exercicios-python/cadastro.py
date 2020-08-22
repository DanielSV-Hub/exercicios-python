nome_usu = str(input('Digite seu nome: '))
idade_usu = int(input('Digite sua idade: '))
if idade_usu > 100:
  print('Opa Matusalém tá em forma!')
elif idade_usu < 10:
  print('Aparentemente você é uma criança prodígio! Parabains!')

print('-' * 30)

email = str(input('Digite seu email: '))
com = '.com'
arroba = '@'
while True: # valida se o endereço de email foi escrito corretamente com um loop while
  if com not in email: # verifica se o ".com" está incluido no email
    print('Seu email deve terminar com ".com"')
    email = str(input('Digite seu email novamente: '))
  elif arroba not in email: # verifica se o "@" está incluido no email
    print('Seu email deve conter "@"')
    email = str(input('Digite seu email novamente: '))
  else:
    print('Email cadastrado com sucesso')
    break

print('-' * 30)

print('Atenção! A senha não pode conter "_" (underline)') # condição da senha: não pode conter "_"
senha = str(input('Digite sua senha: '))
while '_' in senha: # A estrutura se repete enquanto o "_" estiver contido na variável senha
  print('A senha não pode conter "_"')
  senha = str(input('Digite sua senha novamente: '))
  # O comando valida se a senha não contém '_' caso tenha o mesmo irá se repetir até que a senha seja válida
senha_confirm = str(input('Confirme sua senha: '))
if senha_confirm == senha: # Se a senha for igual a sua confirmação o programa segue normalmente
  print('Senha salva')
while senha_confirm != senha: # Enquanto a senha de confirmação for diferente da senha original o programa se repitirá
  print('Erro! As senhas não coincidem, tente novamente.')
  senha_confirm = str(input('Digite a confirmação de senha novamente: '))
print('Cadastro concluído com sucesso!')

print('-' * 30)

l = [] #lista que guarda os dados do usúario 
l.append(email) # O conteúdo da variável email foi adicionado a posição zero da lista 'l'
l.append(senha) # O conteúdo da variável email foi adicionado a posição um da lista 'l'
print('Insira os dados para logar na sua conta!')
email_logar = str(input('Digite seu email: '))
senha_logar = str(input('Digite sua senha: '))
while email_logar != l[0]: # Enquanto o email que loga for diferente do email de cadastro a estrutura se repete
  print('email ou senha não coincidem! tente novamente!')
  email_logar = str(input('Digite seu email: '))
while senha_logar != l[1]: # Enquanto a senha que loga for diferente da senha de cadastro a estrutura se repete
  print('email ou senha não coincidem! tente novamente!')
  senha_logar = str(input('Digite sua senha: '))
# Esse parte de logar foi meio na Gambiarra
print('Logado com sucesso!')
print('Bem-vindo(a) ' + nome_usu + '!')