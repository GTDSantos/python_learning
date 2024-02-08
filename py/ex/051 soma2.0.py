continuar = True
media= 0
soma =0 
quant=0
maior = 0
menor=0
n = int(input('Digite um numero: '))
maior = n
menor = n
while continuar != False:
    n = int(input('Digite um numero: '))
    r = input('Vc deseja comtinuar[S/N]').strip().upper()
    
    
    
    if n > maior:
        maior =n 
    if n< menor:
        menor = n
    
    soma += n
    quant +=1
    media = soma / quant
    
    
    
    
    if r == 'N':
        continuar = False

print ('a media dos numeros é {:.2f}'.format(media))
print ('o maior numero é {}'.format(maior))    

print('O menor numero é {}'.format(menor))