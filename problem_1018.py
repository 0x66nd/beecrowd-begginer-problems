valor = int(input(""))

troco_cem = valor // 100
resto = valor % 100

troco_cinquenta = resto // 50
resto = resto % 50

troco_vinte = resto // 20
resto = resto % 20

troco_dez = resto // 10
resto = resto % 10

troco_cinco = resto // 5
resto = resto % 5   

troco_dois = resto // 2
resto = resto % 2
    
troco_um = resto // 1

print("{}".format(valor))
print("{} nota(s) de R$ 100,00".format(troco_cem))
print("{} nota(s) de R$ 50,00".format(troco_cinquenta))
print("{} nota(s) de R$ 20,00".format(troco_vinte))
print("{} nota(s) de R$ 10,00".format(troco_dez))
print("{} nota(s) de R$ 5,00".format(troco_cinco))
print("{} nota(s) de R$ 2,00".format(troco_dois))
print("{} nota(s) de R$ 1,00".format(troco_um))
