sexo=''
sexo = input('Qual é o seu sexo [M/F]? ').strip().upper()
while sexo not in 'MF':
    print ('vc ditou errado')
    sexo = input('Qual é o seu sexo [M/F]? ').strip().upper()
    
if sexo == 'M':
        print('Sexo Masculino')
else:
        print('Sexo Feminino')