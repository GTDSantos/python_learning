vcasa = int(input('qual é o valor da casa? '))
salario = int(input('qual é o seu salario ? '))
anos = int(input('quantos anos vc vai parcelar ? '))

meses = anos * 12

prest = vcasa/meses

porc = salario*0.30


if prest> porc:
    print('você n pode comprar a casa por utrapassar 30% do seu salario')
else:
    print('você pode comprar a casa pagando R${:.2f} por mes'.format(prest))
