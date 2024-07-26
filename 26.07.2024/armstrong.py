a=int(input())
b=int(input())
for num in range(a,b+1):
    sum=0
    order=len(str(a))
    temp=num
    while temp>0:
        digit=temp%10
        sum=sum+digit**order
        temp=temp//10
    if num==sum:
        print(num)
