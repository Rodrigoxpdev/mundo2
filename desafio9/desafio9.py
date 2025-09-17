# cont = 1 
# while cont <= 10:
#     print(cont, '>' ,end= '')
#     cont += 1
# print('Acabou')

#======================================
#EXEMPLO1 GANBIARA COM S -= 999
# n = s = 0
# while n != 999:
#     n = int(input('Digite um numero: '))
#     s += n
# s -= 999
# print('A soma vale {} '.format(s))




#======================================
#EXEMPLO2 COM BREAK
# n = s = 0
# while True:
#     n = int(input('Digite um numero: '))
#     if n == 999:
#         break
#     s += n
# print('A soma vale {} '.format(s))




#======================================
#EXEMPLO3 COM f string
# n = s = 0
# while True:
#     n = int(input('Digite um numero: '))
#     if n == 999:
#         break
#     s += n
# print('A soma vale {} '.format(s))
# print(f'A soma vale {s}') # F STRING PARA FORMATAR !


#======================================
nome = 'rodrigo'
idade = 26
salario = 1500
print(f'{nome:-^20} tem {idade} anos e ganha {salario:.2f}')

# {nome:-^20} Alinhando nome centro
# {nome:->20} Alinhando nome direita
# {nome:-<20} Alinhando nome esquerda
# {nome:20} colocando espaço entre o nome
#{salario:.2f} formatando casas 























