from random import randrange

n = randrange(0,11)
chute = 0
tet = 0

while chute != n:
    chute =  int(input('Tente adivinha o numero q eu estou Pensando de 1 a 10: '))
    tet += 1
    
print('parabens!!! Vc acertou o numero e precisou de {} tentativas'.format(tet))

