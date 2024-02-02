altura = float(input('qual é sua altura '))
peso = float(input('qual é o seu peso '))

imc = peso / (altura*2)
print ('seu imc é de {0}'.format(imc))
if imc<18.5:
    print('você está abaixo do peso')
elif imc>=18.5 and imc<25:
    print('você está no peso ideal')
elif imc>=25 and imc<30:
    print('você está com sobrepeso')
elif imc>=30 and imc<40:
    print('você está com obesidade')
elif imc>=40:
    print('você está com obesidade mórbida')
