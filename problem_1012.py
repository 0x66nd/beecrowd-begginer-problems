A, B, C = [float(x) for x in input().split()] 

triangulo = A*C/2
print('TRIANGULO: {:.3f}'.format(triangulo))

pi = 3.14159
circulo = pi*C**2
print('CIRCULO: {:.3f}'.format(circulo))

trapezio = (A+B)*C/2
print('TRAPEZIO: {:.3f}'.format(trapezio))

quadrado = B**2      
print('QUADRADO: {:.3f}'.format(quadrado))

retangulo = A*B
print('RETANGULO: {:.3f}'.format(retangulo))
