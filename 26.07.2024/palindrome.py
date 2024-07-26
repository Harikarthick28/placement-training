a=int(input())
temp=a
r=0
while temp>0:
    re=temp%10
    r=r*10+re
    temp=temp//10
print(r)
if (r==a):
    print("palindrome")
else:
    print("not a palindrome")
