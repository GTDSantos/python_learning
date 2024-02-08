maior = 0
menor = 0

for i in range(1,6):
    p = float(input('Escreva o peso da {}º pessoa: '.format(i)))
    if i == 1:
        maior  = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('o maior peso é {}'.format(maior))
print('menor peso é {}'.format(menor))