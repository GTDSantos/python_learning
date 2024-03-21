numeros = ('zero','um', 'dois','tres','quatri','cinco', 'seis','sete','oito','nove','dez','onze','dose','trese','catorse','quinse','deseseis','desesete','desoito','desenove','vinte')
n = int(input('Digite um numero de 0 a 20: '))

while True:
    if n > 20 or n < 0:
        n = int(input('Temte de novo digitar um numero de 0 a 20: '))
    else:
        print('O seu numero por estensso é: {}'.format(numeros[n]))
        break