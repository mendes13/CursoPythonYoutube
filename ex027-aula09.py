nome = input('Digite o seu nome completo!').title()
nomex = nome.split()
print('O seu nome completo é = {}'.format(nome))
print('Primeiro nome = {}'.format(nomex[0]))
print('Segundo nome = {}'.format(nomex[len(nomex)-1]))
