input_str = input("Enter the elements of the array separated by spaces: ")
array = list(map(int, input_str.split()))
if array:
    max_element = array[0]
    for num in array:
        if num > max_element:
            max_element = num
else:
    max_element = None
print(f"The maximum element in the array is: {max_element}")
