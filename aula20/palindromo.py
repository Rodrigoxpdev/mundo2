#PALINDROMO

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()#com espaço
junto = "".join(palavras)#sem espaço
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso+=junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALINDROMO!')
else:
    print('O Nome não é um PALINDROMO!')





















