user_input = input("Enter a list of items separated by spaces: ").split()

unique_item = set()

for item in user_input:
    if item in unique_item:
        print("Duplicate Detected:", item)
        break
    unique_item.add(item)
else:
    print("No Duplicates Found")
