# AREA DE TESTE
from math import factorial


n = int(input('Digite um numero para calcular seu fatorial: '))
f = factorial(n)
c = n
f = 1



while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else '=', end='')
    c -= 1
# print('o fatorial de: {} é {}'.format(n , f))

















