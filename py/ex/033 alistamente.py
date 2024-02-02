ano = int(input('em q ano vc naceu: '))

idade = 2024 - ano

if idade < 18:
    print('vc ainda vai ter q se alistar e faltao {} anos para o alistamento'.format(18-idade))
elif idade == 18:
    print('vc tem que se alistar esse ano')
else:
    print('vc ja passou do tempo de alistamento ja fazem {} anos'.format(idade-18))