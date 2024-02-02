from random import randrange

print('seu objetivo e acertar o numero q eu estou pessando')
n = randrange(5)+1
nresposta = int(input ('escolha um numero q eu estou pessando de 1 a 5: '))
if nresposta == n:
    print('você acertou o numero era {} mesmo'.format(n))
else:
    print('você errou o numero q eu estou pessando é {}'.format(n))