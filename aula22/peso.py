
maior = 0  #primeira ocorrencia
menor = 0  #segunda ocorrenncia

for p in range(1,6):
    peso = float(input("peso da {} pessoa: ".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso lido foi de {}kg'.format(maior))
print('o menor peso foi de {}kg '.format(menor))






































