nome = str(input('Digite o seu nome: '))  # pede o nome do usuário em formato str
while len(nome) < 3:  # enquanto o len da variável nome for menor do que três o programa se repete
    print('Nome inválido. Tente novamente.')
    nome = str(input('Digite o seu nome: '))
idade = int(input('Digite sua idade: '))
while idade < 0 or idade > 150:
    print('Idade inválida. Tente novamente.')
    idade = int(input('Digite sua idade: '))
sal = int(input('Digite seu salário: '))
while sal <= 0:
    print('Salário inválido. Tente novamente.')
    sal = int(input('Digite seu salário: '))