#SEQUENCIA DE FIBONACCI

print('__'*20)
print('Sequencia de Fibonacci')
print('__'*20)
n1 =  int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1 
print('__'*20)
print('{} > {} '.format(t1, t2), end= '')
cont  = 3
while cont <= n1:
    t3 =  t1 + t2
    print('> {} '.format(t3), end= '')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')











































