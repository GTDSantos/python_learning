from random import randrange

n = (randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10))

print('os numeros gerados foram: {}'.format(n))

ordem = sorted(n)

print('O maior numero é: {}'.format(ordem[-1]))
print('O menor numero é: {}'.format(ordem[0]))
