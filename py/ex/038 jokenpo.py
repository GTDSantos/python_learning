from random import choice

escolha = input('escreva pedra, papel ou tisoura para ver quem ganha no jokenpo: ')

escolha = escolha.lower()

escolhacop = choice(['pedra','papel','tisoura'])

print ('vc escolheu {} eu escolhi {}'.format(escolha, escolhacop))

if escolha == escolhacop:
    print('empate')
elif escolha == 'pedra' and escolhacop == 'tisoura':
    print('vc ganhou')
elif escolha == 'papel' and escolhacop == 'pedra':
    print('vc ganhou')
elif escolha == 'tisoura' and escolhacop == 'papel':
    print('vc ganhou')
elif escolhacop == 'pedra' and escolha == 'tisoura':
    print('vc perdeu')
elif escolhacop == 'papel' and escolha == 'pedra':
    print('vc perdeu')
elif escolhacop == 'tisoura' and escolha == 'papel':
    print('vc perdeu')
else:
    print('vc escreveu errado burro')