#PROGRESAO ARITIMETICA
#TEMPORIZADOR
from time import sleep

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

print('=='*20)
sleep(1.5)
print('ANALISANDO...')
print('=='*20)

sleep(2.3)
print('=='*30)
for c in range(primeiro, decimo+razao , razao):
    print('{} '.format(c), end=' > ')
print('ACABOU!')
print('=='*30) 































