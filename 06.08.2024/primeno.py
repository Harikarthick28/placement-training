a=int(input())
flag=False
if(a==1):
    print("it is not a prime") 
elif(a>1):
    for i in range(2,a):
        if(a%i)==0:
            flag=True
            break
    if flag:
        print(a,"is not a prime")
    else:
        print(" it is a prime number")
