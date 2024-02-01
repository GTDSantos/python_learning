n1 = int(input('quantos dias vc ficou com o carro ? '))
n2 = int(input("quantos quilometros foram rodados ? "))
r1 = n1*60
r2 = n2*0.15
r = r1+r2
print ('o valor do aluguel ficou de R${:.2f}'.format(r))