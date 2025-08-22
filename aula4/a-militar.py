# Alistamento militar
from datetime import date
atual = date.today().year
nascimento = int(input("Ano de nascimento? "))
idade = atual - nascimento
print("Quem nasceu em {} tem {} anos em {}".format(nascimento, idade, atual))

sexo = input("Seu sexo? [masculino/feminino] ").strip().lower()
if sexo == "masculino":
    if idade == 18:
        print("Você tem que se alistar IMEDIATAMENTE!")
    elif idade < 18:
        saldo = 18 - idade
        print("Ainda faltam {} anos para o alistamento".format(saldo))
        ano = atual + saldo
        print("seu alistamento foi em {} ano".format(ano))
    elif idade > 18:
        saldo = idade - 18
        print("Você já deveria ter se alistado há {} anos".format(saldo))
        ano = atual - saldo
        print("seu alistamento foi em {} ano".format(ano))

else:
    print("Alistamento militar obrigatório apenas para pessoas do sexo masculino.")

