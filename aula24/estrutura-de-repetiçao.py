# c = 1 #contador começando em 1

# while c < 10: #contador menor que 10
#     print(c)
#     c = c +1 
# print('fim')



#EXEMPLO 2
# n =1 #se for diferente de 0 faça, se for 0 pare o programa

# while n != 0:
#     n = int(input('Digite um valor: '))
# print('fim')


#exemplo 3
# r = 'S' #RESPOSTA

# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar? [S/N] ')).upper() 
# print('fim')


#exemplo 4
n =1
par = impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('voce digitou {} numeros pares e {} numeros impares'.format(par, impar))
































