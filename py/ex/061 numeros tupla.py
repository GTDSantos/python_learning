n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite outro numero: "))
n4 = int(input("Digite outro numero: "))

numeros = (n1, n2, n3, n4)

print('Vc digitou os numeros: {}'.format(numeros))

nove = numeros.count(9)
if nove != 0:
    print('Apareceu o numero 9, {} vezes'.format(nove))
else:
    print('Vc não digitou 9 nenhuma vez')


ctres = numeros.count(3)
if ctres != 0:
    tres = numeros.index(3) + 1
    print('O numeor tres aparece na posição: {}'.format(tres))
else:
    print('Vc não digitou o mumero 3')

par = ''

for n in numeros:
    if n % 2 == 0:
        par = par + ' '+str(n)

print("Os numeros pares são: {}".format(par))




print('')
