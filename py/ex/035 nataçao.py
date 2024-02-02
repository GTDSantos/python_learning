idade = int(input('qual é sua idade: '))

if idade <= 9:
    print('Vc é um atleta mirim')
elif idade> 9 and idade <= 14:
    print ('Vc é um atlet infantil')
elif idade>14 and idade <=19:
    print('Vc é um atlet junior')
elif idade>19 and idade <=20:
    print('Vc é um atlet senior')
elif idade>20:
    print('Vc é um atleta master')