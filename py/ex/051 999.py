r=0
quant=0
n= int(0) 
while n != 999:
    n = int(input('escreva numeros para somar, quando quiser parar digete 999: '))
    r += n
    quant+=1
quant = quant - 1
r = r -999
print ('a soma de todos os numeros deu: {}'.format(r))
print('vc usou {} numeros'.format(quant))

