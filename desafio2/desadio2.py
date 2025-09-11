# JOGO DE ADVINHAÇAO MELHORADO!

from random import randint

computador = randint(0, 10)
print('Sou seu computador acabei de pensar em um numero entre 0 e 10')
print('Será que você consegue advinhar qual foi? ')
acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente outra vez!')
        elif jogador > computador:
            print('Menos... tente outra vez!')
print('Acertou com {} tentativas parabéns '.format(palpite))









































