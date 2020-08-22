coisa = str(input('Digite uma palavra que não tenha a letra "G": ')).upper()
while 'G' in coisa:
  print('A mensagem não podia ter a letra "G", tente novamente espertinho.')
  coisa = str(input('Digite uma palavra que não tenha a letra "G": ')).upper()
print('Ok! Mensagem válida!')