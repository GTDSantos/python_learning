m=0
me=0
ida = 0
for v in range(1,7):
    ida = int(input('Escreva o ano da {}º pessoa: '.format(v)))
    if (2024 - ida)>=18:
        m += 1
    else:
        me += 1

print('A quantidade de pessoas maiores de idade é: {}'.format(m))
print('A quantidade de pessoas menores de idade é: {}'.format(me))