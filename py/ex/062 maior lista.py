num = []

n1 = num.append(int(input('digite um valor: ')))
n2 = num.append(int(input('digite outro valor: ')))
n3 = num.append(int(input('digite outro valor: ')))
n4 = num.append(int(input('digite outro valor: ')))
n5 = num.append(int(input('digite outro valor: ')))


numa = num[:]

numa = sorted(numa)

print(num)
maior = numa[-1]
menor = numa[0]

ps1 = num.index(maior) + 1
ps2 = num.index(menor) + 1


print('O maior numero é {} e esta na posisão {}'.format(maior,ps1))
print('O menor numero é {} e esta na posisão {}'.format(menor,ps2))