total = 0
mil = 0
nbarato = ''

while True:
    nome = input('Qual é o nome do produto: ')
    
    nbarato = nome 
    
    valor = float(input('Qual é o valor do produto: '))
    
    barato = valor
    
    r = str(' ')
    while r not in 'SN':
        r = input('Quer continuar [S/N]').strip().upper()
    
    total = total + valor
    
    if valor>= 1000:
        mil += 1
    
    
    if valor < barato:
        barato = valor
        nbaratos = nome
        
    
    if r == 'N':
        break
    print('================================================================')

print('O total gasto foi de R${}'.format(total))
print('{} produtos custao mais de R$1000'.format(mil))
print('O nome do produto mais barato é {} e custa R${}'.format(nbarato, barato))

print('================================================================')
  
    