cidade = input("digite o nome de umas cidade: ")

cidade = cidade.lower()
cidade = cidade.split()
print ('sua cidade começa com santo: {}'.format('santo' in cidade[0]))