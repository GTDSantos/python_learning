n = int(input('Digite o valor da compra: '))

sinquente = 0
vinte = 0
deis = 0 
sinco = 0
um = 0



while True:
    if n > 50:
        n -= 50
        sinquente +=1
    else:
        break
while True:
    if n > 20:
        n -= 20
        vinte +=1
    else:
        break
while True:
    if n > 10:
        n -= 10
        deis +=1
    else:
        break
while True:
    
    if n > 5:
        n-=5
        sinco +=1
    else:
        break
while True:
    if n > 1:
        n-=1
        um +=1
    else:
        break 
    
    

print ('================================================================')
print('Vc usou {} notas de R$50'.format(sinquente))
print ('Vc usou {} notas de R$20'.format(vinte))
print('Vc usou {} notas de R$10'.format(deis))
print('Vc usou {} notas de R$5'.format(deis))
print('Vc usou {} notas de R$1'.format(um))
        