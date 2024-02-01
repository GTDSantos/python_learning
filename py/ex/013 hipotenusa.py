from math import sqrt 

n1 = float(input('digite o cateto oposto: '))
n2 = float(input('digite o cateto adiacente: '))
r = sqrt((n1**2 + n2**2))
print ('a hipotenusa é {}'.format(r))