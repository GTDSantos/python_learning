from random import randrange

vl = randrange(180)+1

if vl > 80:
    print('você andou a {}km tomouma multa de R${}'.format(vl,(vl-80)*7))
else:
    print('você não tem multa pois andou a {}km'.format(vl))