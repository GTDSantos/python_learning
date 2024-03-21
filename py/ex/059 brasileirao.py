times = ('Palmeiras', 'Gremio', 'Atletico-mg', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminence', 'Atletico-pr',
         'Internacional', 'Fortaleza', 'Sao Paulo', 'Cuiaba', 'Corintians', 'Cruseiro', 'Vasco', 'Bahia',
         'Santos', 'Goias', 'Coritiba', 'America')
print("Os primeiros 5 colocados sao: {}".format(times[0:5]))

print('=' * 50)

print('Os quatro ultimos colocados são: {}'.format(times[-4:]))

print('=' * 50)

print('A lista de times em ordem alfabetica é: {}'.format(sorted(times)))

print('=' * 50)

print('O coritiba esta na posição: {}'.format(times.index('Coritiba')+1))
