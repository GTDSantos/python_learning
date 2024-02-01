from math import ceil
import emoji


n1 = int(input('qual é a altura da parede ? '))
n2 = int(input('qual é a largura da parede ? '))
print ('presisara de {} baldes de tinta'.format(ceil((n1 * n2)/2)))
print(emoji.emojize('thumbs_up:'))