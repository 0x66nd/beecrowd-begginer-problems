dias = int(input(''))

anos = dias // 365
resto = dias % 365
meses = resto // 30
dias = resto % 30

print('{} ano(s)\n{} mes(es)\n{} dia(s)\n'.format(anos, meses, dias))