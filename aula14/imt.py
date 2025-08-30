#SOMANDO IMPARES MULTIPLOS DE3
soma = 0 #soma dos numeros 
cont = 0 #contador 

for x in range(1, 501, 2): #laço de repetiçao entre 1 a 500 pulando de 2 em 2
    if x % 3 ==0:
        cont = cont + 1 #contador forma mais estendida
        soma += x #acumulador forma simplificada
print("O Resultado total de todos os {} valores solicitados é {} : ".format(cont, soma))


















































