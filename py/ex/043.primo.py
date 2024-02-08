a=0
tot =0
n =int(input("digete um numero: "))

for i in range(0,n):
    a = a +1
    if n % a ==0:
        
        tot += 1
      
if tot == 2:
    print('esse numero é primo')
else:
    print('esse numero nao é primo')   
