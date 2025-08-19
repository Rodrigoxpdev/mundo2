# CONVERSOR DE BASES
# PERGUNTA
num = int(input('Digite um numero inteiro '))

#RESPOSTA
print("--"*25) 
print("Escolha uma das bases para conversão: " )
print(" [ 1 ] converter para BINARIO") 
print(" [ 2 ] converter para OCTAL") 
print(" [ 3 ] converter para HEXADECIMAL""")
print("--"*25) 
opçao = int(input("Sua opção: "))

#CONDIÇÕES
if opçao == 1:
    print("--"*25) 
    print("{} convertido para BINARIO é igual a {} ".format(num, bin(num)[2:]))
    print("--"*25) 
elif opçao == 2:
    print("--"*25) 
    print("{} convertido para OCTAL é igual a {}".format(num, oct(num)[2:]))
    print("--"*25) 
elif opçao == 3:
    print("--"*25) 
    print("{} convertido para OCTAL é igual a {}".format(num, hex(num)[2:]))
    print("--"*25) 
else:
    print("--"*25) 
    print("Opção invalida. Tente novamente.")
    print("--"*25) 


























































