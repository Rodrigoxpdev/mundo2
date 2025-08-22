# ANALISANDO TRIANGULOS

#PERGUNTAS
s1 = float(input("Primeiro segmento: "))
s2 = float(input("Segundo segmento: "))
s3 = float(input("Terceiro segmento: "))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("OS SEGMENTOS ACIMA PODEM FORMAR TRIANGULO! ",end='' ) 
    if s1 == s2 == s3:
        print("EQUILATERO")
    elif s1 != s2 != s3 != s1:
        print("ESCALENO") 
    else:
        print("ISOSCELES") 
else:
    print("OS SEGMENTOS ACIMA NÃO PODEM FORMAR TRIANGULO!")
    
#FIM DO PROGRAMA...