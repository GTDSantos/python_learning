
mais = 0
home = 0
mue = 0

while True:
    print('================================================================')
    print ('                           Cadastro')
    print('================================================================')

    idade = int(input("Quantos Anos: "))
    if idade >= 18:
        mais += 1
        
    sexo = ' '
    while sexo not in 'MF':
            sexo = str(input('Qual é o seu sexo [M/F]? ')).strip().upper()[0]
        
    if sexo == 'M':
        home += 1
            
    if idade > 20 and sexo == 'F':
        
        mue += 1
    r = ' '
    while r not in 'SN':
        r = input('Deseja continuar [S/N]: ').strip().upper()
    
    
    if r == 'N':
        break

print ('{} sao maiores de 18 anos'.format(mais))
print('Tem {} homens cadastrados'.format(home))
print ('Tem {} mulhers com menos de vinte anos'.format(mue))