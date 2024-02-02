from random import randrange
km = randrange(600)

if km > 200:
    print ('sua viagem foi de {}km o presso diminuira para R$0.45 por km por isso pagara R${:.2f}'.format(km, km*0.45))
else:
    print ('sua viagem foi de {}km o presso ficara R$0.50 por km por isso pagara R${:.2f}'.format(km, km*0.50))