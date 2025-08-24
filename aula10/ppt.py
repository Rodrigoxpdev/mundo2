#PEDRA PAPEL TESOURA 
from queue import SimpleQueue
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''  
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!!')

print('-='*15)
print('Computador jogou {} '.format(itens[computador]))
print('Jogador jogou {} '.format(itens[jogador]))
print('-='*15)

if computador == 0: #PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("Jogada invalida!")
elif computador == 1: #PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador ==1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print("Jogada invalida!")
elif computador == 2: #TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print("Jogada invalida!")





























