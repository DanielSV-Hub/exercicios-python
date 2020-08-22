l = list()
n = str(input('Digite sua expressão: '))
for simb in n:
    if simb == '(':
        l.append('(')
    elif simb == ')':
        if len(l) > 0:
            l.pop()
        else:
            l.append(')')
            break
if len(l) == 0:
    print('Expressão Ok!')
else:
    print('Algo de errado não está certo!')