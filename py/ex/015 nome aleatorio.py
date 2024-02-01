from random import choice, shuffle
r = choice(['sara', 'ema', 'jef'])
print ('entre sara, ema e jaf o escolido sera {}'.format(r))
nomes = 'sara ema jaf'.split()
shuffle(nomes)
print ('e tera uma ordem de {}'.format(nomes))
