n1 = int(input('escreva um numero'))
n2 = int(input('escreva um numero'))

if n1 > n2:
    print('O {} é maior'.format(n1))
    print('O {} é menor'.format(n2))
elif n1 < n2:
    print('O {} é maior'.format(n2))
    print('O {} é menor'.format(n1))
elif n1 == n2:
    print('O {} é igual a {}'.format(n1, n2))