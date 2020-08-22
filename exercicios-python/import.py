import math
x = int(input('Digite o valor do ângulo(°): '))
y = math.cos(x)
z = math.sin(x)
w = math.tan(x)
print(f'O Cosseno desse ângulo é {y:.2f}, seu Seno é {z:.2f} e sua Tangente é {w:.2f}')