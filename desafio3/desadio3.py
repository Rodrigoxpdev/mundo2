#  MENU DE OPÇOES
from time import sleep

# PERGUNTAS
n1 = int(input('Primeiro valor? '))
n2 = int(input('Segundo valor? '))

#CALCULOS 
opçao = 0

# OPÇOES
while opçao != 5:
    print(''' 
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa ''')
# OPÇAO PERGUNTA
    opçao = int(input('Qual é a sua opção '))
    if opçao == 1:
        soma = n1+n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opçao ==  2:
        produto = n1*n2
        print('O Resultado de {} x {} é {}'.format(n1,n2,produto))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior= n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2 , maior))
    elif opçao == 4:
        print('Informe os numeros novamente: ')
        n1= int(input('Primeiro valor: '))
        n2= int(input('Segundo valor: '))
    elif opçao == 5:
        print('Finalisando...')
    else:
        print('Opção invalida. tente novamente!')
    print('=-='*20)
    sleep(1.2)
print('Fim do program Volte sempre!')





































