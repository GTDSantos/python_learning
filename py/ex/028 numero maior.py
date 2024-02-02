n1 = int(input('escolha um numero: '))
n2 = int(input('escolha um numero: '))
n3 = int(input('escolha um numero: '))

if n1 > n2 and n1 > n3:
    print('{} é o maior'.format(n1))

elif n2 > n1 and n2 > n3:
    print('{} é o maior'.format(n2))
else:
    print('{} é o maior'.format(n3))
    
    
if n3 < n1 and n3 < n2:
    print('{} é o menor'.format(n3))

elif n2 < n1 and n2 < n3:
    print('{} é o menor'.format(n2))
else:
    print('{} é o menor'.format(n1))