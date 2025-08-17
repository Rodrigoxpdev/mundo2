#APROVANDO EMPRESTIMO

#PERGUNTAS
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Quanto é seu salario? R$'))
anos = int(input('Em quantos anos você quer pagar? '))

#CALCULOS
prestaçao = casa / (anos * 12)
minimo = salario*30 / 100 #30 por cento do salario

#RESPOSTAS
print('__'*20)   
print("para comprar uma casa de R${:.2f} em {}x ".format(casa, anos), end='' )
print("a prestaçao será de R${:.2f}".format(prestaçao))
print('__'*20)  

#CONDIÇÕES
if prestaçao <= minimo:

    print('__'*20)   
    print("EMPRESTIMO pode ser CONCEDIDO!")
    print('__'*20)   

else:
    print('__'*20)   
    print("Emprestimo NEGADO!")
    print('__'*20)    


