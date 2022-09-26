x = int(input(""))
y = int(input(""))

resultado = 0

if x > y and x % 2 == 0:
    aux = x - 1
    while aux > y:
        resultado += aux
        aux -= 2

elif x > y and x % 2 == 1:
    aux = x - 2
    while aux > y:
        resultado += aux
        aux -= 2
        
elif y > x and y % 2 == 0:
    aux = y - 1
    while aux > x:
        resultado += aux
        aux -= 2
else:
    aux = y - 2
    while aux > x:
        resultado += aux
        aux -= 2
    
print(resultado)
