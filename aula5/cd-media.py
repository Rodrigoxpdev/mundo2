#PERGUNTAS
nota1 = float(input(" PRIMEIRA MEDIA: "))
nota2 = float(input(" SEGUNDA MEDIA: "))

#CALCULO
media = (nota1 + nota2) / 2

#RESPOSTA 
print("Tirando {:.1f}, e {:.1f} a média do aluno é {:.1f}".format( nota1, nota2, media))

#CONDIÇOES
if media >= 5 and media < 7:
    print("O aluno está em RECUPERAÇAO!")
elif media < 5:
    print("O aluno está REPROVADO!")
elif media > 7:
    print("O aluno está APROVADO!")














