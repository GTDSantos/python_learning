r1 = int(input('escolha um comprimento: '))
r2 = int(input('escolha um comprimento: '))
r3 = int(input('escolha um comprimento: '))

if r1+r2> r3 and r1+r3> r2 and r3+r2> r1:
    print('da pra formar um triandolo')
    
    if r1==r2==r3:
        print('triangulo equilatero')
    elif r1==r2 or r1==r3 or r2==r3:
        print('triangulo isosceles')
    elif r1!=r2 or r1!=r3 or r2!=r3:
        print('triangulo escaleno')
        
    
    
    
else:
    print('nao formar um triangulo')
    
    
    