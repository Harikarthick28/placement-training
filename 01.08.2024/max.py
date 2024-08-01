arr=[]
n=int(input("Enter no of elmts:"))
for i in range(n):
    a=int(input())
    arr.append(a)
print(arr)
max_element=arr[0]
for num in arr:
    if num>max_element:
        max_element=num
print("the maximum element is:",max_element)
