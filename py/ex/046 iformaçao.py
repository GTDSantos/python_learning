media = 0
soma = 0
maior = 0
mnome = ''
fmenor = 0

for t in range(1,6):
    print ('==================={}==================='.format(t))
    nome = input('Qual é o seu nome: ')
    idade = int(input('Qual é a sua idade: '))
    sexo = input('Qual é o seu sexo [M/F]: ').upper()
    soma = soma + idade
    if sexo == 'M':
        if t == 1:
            mairo = idade
            mnome = nome
        else:
            if idade > maior:
                maior = idade
                mnome = nome
    else:
        if idade < 20:
            fmenor += 1
media = soma / 4 
print ('================================================================')
print('a media de idade dos candidatos é {}'.format(media))
print('o homem mais velho é {}'.format(mnome))
print('tem {} mulheres com menos de 20 anos'.format(fmenor))
    