#CALCULANDO ImC

#PERGUNTAS
peso = float(input("Qual seu peso? "))
altura = float(input("Qual sua altura? "))

#CALCULOS
imc = peso / ( altura **2)
print("--"*20)
print("O IMC dessa pessoa é de {:.1f}".format(imc))
print("--"*20)


#CONDIÇÔES 
if imc < 18.5:
    print("--"*20)
    print("Você está ABAIXO DO PESO normal")
    print("--"*20)
elif 18.5 <= imc < 25:
    print("--"*20)
    print("Parabens você está na faixa de PESO NORMAL")
    print("--"*20)
elif 25 <= imc < 30:
    print("--"*20)
    print("Você está em SOBREPESO!")
    print("--"*20)
elif imc >= 40:
    print("--"*20)
    print("Você está em OBESIDADE MORBIDA, CUIDADO!")
    print("--"*20)




















