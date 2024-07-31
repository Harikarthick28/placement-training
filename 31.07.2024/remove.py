my_list = [1, 2, 3, 4, 5]
value_to_remove = 3
if value_to_remove in my_list:
    my_list.remove(value_to_remove)
    print(f"Removed {value_to_remove}. Updated list: {my_list}")
else:
    print(f"Value {value_to_remove} not found in the list.")
