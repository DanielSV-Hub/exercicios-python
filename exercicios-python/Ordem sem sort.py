l = list()
for x in range(0, 5):
    y = int(input('Digite um valor: '))
    if x == 0 or y > l[-1]:
        l.append(y)
    else:
        pos = 0
        while pos < len(l):
            if y <= l[pos]:
                l.insert(pos, y)
                break
            pos += 1
print(l)