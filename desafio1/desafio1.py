
sexo =str(input('Digite o sexo [F/M]: ')).upper()[0]

while sexo not in 'FfMm':
    sexo=str(input('dados invalido digite novamente: ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))









































