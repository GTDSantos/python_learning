from time import sleep
from random import randrange
pc = randrange(1,6)
vitorias =0 
while True:
    escolha = input('Digite [1] pra par e [2] para impar: ')
    n = int(input('Escolha um numero: '))
    print('Par!!')
    sleep(1)
    print('Ou')
    sleep(1)
    print('Impar!!')
    sleep(1)
    print('Pc= {} --- Vc= {}'.format(pc,n))
    sleep(1)
    
    
    if escolha == '1':
        if (n+pc)%2 == 0:
            print('Vc ganhou')
            vitorias += 1
        else:
            print('Vc perdeu')
            break
    if escolha == '2':
        if (n+pc)%2!= 0:
            print('Vc ganhou')
            vitorias += 1
        else:
            print('Vc perdeu')	
            break
if vitorias > 0:
    print('Você ganhou {} vezes'.format(vitorias))
else:
    print('')