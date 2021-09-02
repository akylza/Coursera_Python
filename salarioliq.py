metros = int(input('Qual o tamanho (em metros quadrados) da área a ser pintada? '))
cobtinta = metros / 3


if tamanho <= 54:
	latas = tamanho / 54
else: 
	latas = int(tamanho / 54) + 1

preco = latas * 80
print ('%d latas' %latas)
print ('R$ %.2f' %preco)


