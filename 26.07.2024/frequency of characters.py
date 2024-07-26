a=input()

af= {}
 
for i in a:
    if i in af:
        af[i] += 1
    else:
        af[i] = 1

print(af)
