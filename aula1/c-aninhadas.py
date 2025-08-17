#condiçóes aninhadas
#PERGUNTAS
nome = str(input("Qual é seu nome? "))

#CONDIÇÕES
if nome == 'Rodrigo':
    print("que nome bonito")
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print("Seu nome é bem popular no brasil {} ".format(nome))
    
elif nome in 'Ana claudia jessica guilherme cassio bela theo':
    print("---"*20)
    print('seu nome esta na lista {}'.format(nome))
    print("---"*20)

else:
    print("---"*20)
    print("SEU NOME NÃO ESTÁ NA LISTA {}".format(nome ))
    print("---"*20)





















