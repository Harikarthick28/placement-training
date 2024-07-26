def get_input(a="enter an integer:"):
    while True:
        input=a(int)
        try:
            value=int(input)
            return value
        except ValueError:
            print("invalid integer")
get_integer=get_input()
print(f"you entered{get_integer}")
