metros = float(input('Qual o tamanho (em metros quadrados) da área a ser pintada? '))
cobtinta = int(metros / 6)
print('O consumo de tinta é de ', cobtinta, 'litros')

latas18 = int(cobtinta / 18)
galão3 = int(cobtinta / 3.6)
print('Você irá precisar de ', latas18, 'latas de 18 litros cada')
print ('Você irá precisar de ', galão3, 'galões de 3.6 litros cada')

valorlatas18 = int(80 * latas18)
valorgalão3 = int(25 * galão3)
print('Caso opte por comprar somente latas de 18 litros, você irá gastar R$', valorlatas18)
print('Caso opte por comprar somente galões de tinta de 3.6 litros, você irá gastar R$', valorgalão3)




