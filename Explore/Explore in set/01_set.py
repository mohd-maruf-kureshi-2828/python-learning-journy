my_set = set()

# Step 2: Insert elements
for i in range(5):
    val = input(f"Enter element {i+1}: ")
    my_set.add(val)

print("Current Set:", my_set)

# Step 3: Delete an element
delete_val = input("Enter an element to delete: ")
if delete_val in my_set:
    my_set.remove(delete_val)
    print(f"{delete_val} deleted.")
else:
    print(f"{delete_val} not found.")

# Step 4: Find position
search_val = input("Enter an element to find its position: ")
if search_val in my_set:
    temp_list = list(my_set)
    print(f"Position of {search_val}: {temp_list.index(search_val)}")
else:
    print("-1 (Not Found)")
