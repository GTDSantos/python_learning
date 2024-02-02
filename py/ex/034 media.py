nota = int(input('quanto vc tirou na primeira prova: '))
nota2 = int(input('quanto vc tirou na segunda prova: '))

media = (nota + nota2) / 2

if media < 50:
    print('reprovado')
elif media >= 50 and media <= 69:
    print('recuperacao')
elif media >= 70:
    print('aprovado')