pesopeixe = int(input('Quantos quilos de peixe você tem? '))

if pesopeixe <= 50:
    print('Oba! Sua carga está no peso ideal. Não há multa!')
else:
    excesso = pesopeixe - 50
    multa = excesso * 4
    print('Eita! Sua carga ultrapassou ', excesso, 'kgs. Sua multa será no valor de R$ ', multa, 'reais')



