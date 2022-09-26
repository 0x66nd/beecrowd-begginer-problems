n = int(input(""))

in_interval = 0
out_interval = 0

for i in range(n):
    
    x = int(input(""))
    
    if x >= 10 and x <= 20:
        in_interval += 1
    else:
        out_interval += 1
        
print("{} in\n{} out".format(dentro, fora))