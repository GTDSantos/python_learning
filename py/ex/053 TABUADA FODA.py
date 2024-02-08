n= 0
while True:
    n = int(input('Escolha um numero para a tabuada: '))
    print('===========================')
    if n <0:
        print('Fim')
        break
        
    for t in range(1,11):
        print('{} X {} = {}'.format(n,t,(n*t)))
    print('===========================')
    