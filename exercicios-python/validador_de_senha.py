print('Atenção! A senha não pode conter "_"')
senha = str(input('Digite sua senha: '))
while '_' in senha:
  print('A senha não pode conter "_"')
  senha = str(input('Digite sua senha novamente: '))
  # O comando valida se a senha não contém '_' caso tenha o mesmo irá se repetir até que a senha seja válida
senha_confirm = str(input('Confirme sua senha: '))
if senha_confirm == senha:
  print('Senha salva')
while senha_confirm != senha:
  print('Erro! As senhas não coincidem, tente novamente.')
  senha_confirm = str(input('Digite a confirmação de senha novamente: '))
print('Cadastro concluído com sucesso!')