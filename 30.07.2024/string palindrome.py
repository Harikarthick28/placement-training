s = input("Enter a string: ")
cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
if cleaned_s == cleaned_s[::-1]:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")
