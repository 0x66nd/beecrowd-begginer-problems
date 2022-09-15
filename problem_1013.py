a, b, c = [int(x) for x in input().split()] 
maior = (a+b+abs(a-b))/2
maior = (maior+c+abs(maior-c))/2
print('The greatest number is {:.0f}'.format(maior))
