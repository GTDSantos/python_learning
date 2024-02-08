quant=0
soma=0


while True:
    n = int(input('escreva um numero: '))
    if n == 999:
        break
    quant+= 1
    soma = soma + n

print('vc usou {} numeros'.format (quant))
print('A soma deu {}'.format (soma))