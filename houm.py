sexo = int(input('Você é homem ou mulher? (1- Homem / 2- Mulher): '))
h = float(input('Qual a sua altura? '))

if sexo == 1:
    pesoideal = (72.7*h) - 58
else:
    pesoideal = (62.1*h) - 44.7
    
print('Você tem ', h, 'de altura. O seu peso ideal é ', pesoideal)



