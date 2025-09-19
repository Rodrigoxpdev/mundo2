# PAR OU INPAR
from random import randint
v = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. total de {total}')
    print('DEU PAR ' if total % 2 == 0 else 'DEU IMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('você VENCEU!')
            v += 1
        else:
            print('você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('você VENCEU!')
            v += 1
        else:
            print('você PERDEU!')
            break
    print('Vamos jogar novamente.. ')
print(f'GAME OVER! Você venceu {v} vezes.')
