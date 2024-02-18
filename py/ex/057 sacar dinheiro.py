sac = int(input('Que valor vc quer sacar: '))
total = sac
sinque = 0
vinte = 0
sinco = 0
um = 0

while True:
        if total >=50:
            total = total - 50
            sinque +=1
        else:
            break
while True:
        if total >=20:
            total = total - 20
            vinte +=1
        else:
            break
    
while True:
        if total>=5:
            total = total - 5
            sinco +=1
        else:
            break
    
while True:
        if total >=1:
            total = total - 1
            um +=1
            
        else:
            break
    

print ('================================================================')
print ('Vc usou {} notas de R$50'.format(sinque))
print('Vc usou {} notas de R$20'.format(vinte))
print('Vc usou {} notas de R$5'.format(sinco))
print('Vc usou {} notas de R$1'.format(um))

    
    