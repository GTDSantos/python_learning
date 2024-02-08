sair = False
op =0 
res =0
while sair != True:
    n1 = int(input('Escolha um numero: '))
    n2 = int(input('Escolha outro numero: '))
    op +=1
    print('Escolha uma opção: ')
    print('Escolha [1] para somar'.format(op))
    print('Escolha [2] para subitrair'.format(op))
    print('Escolha [3] para multiplicar'.format(op))
    print('Escolha [4] para dividir'.format(op))
    print('Escolha [5] para sair'.format(op))
    r =int(input('escreva o numero da sua ação: '))
    if r == 1:
        res = n1 + n2
    elif r == 2:
        res = n1 - n2
    elif r == 3:
        res = n1*n2
    elif r==4:
        res = n1/n2
    elif r==5:
        sair = True
    else:
        
        print('nao existe essa opção')
    print('o resultado da sua ação é {}'.format(res))
    
    
    
    