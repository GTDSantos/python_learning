soma = 0
n =0

for s in range(1,7):
    n = int(input('escreva um numero: '))
    if n % 2 == 0:
        soma += n

print('a soam dos numeros pares é: {}'.format(soma))