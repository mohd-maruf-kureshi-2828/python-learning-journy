my_dict = {}

# Step 2
name = input("Enter your name: ")
email = input("Enter your email: ")
mobile = input("Enter your mobile number: ")
city = input("Enter your city: ")
pin = input("Enter your pin code: ")

# Step 3
my_dict['name'] = name
my_dict['email'] = email
my_dict['mobile'] = mobile
my_dict['city'] = city
my_dict['pin'] = pin

# Step 4
print("\n--- User Details ---")
for key, value in my_dict.items():
    print(f"{key} : {value}")

# Step 5
new_name = input("\nEnter a new name to replace old one: ")
my_dict['name'] = new_name

# Step 6
key_to_remove = input("\nEnter a key to delete: ")
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"{key_to_remove} removed successfully.")
else:
    print(f"{key_to_remove} not found in dictionary.")

# Step 7
value_check = input("\nEnter a value to check in dictionary: ")
if value_check in my_dict.values():
    print("Yes, value exists ✅")
else:
    print("No, value doesn't exist ❌")

# Step 8
state = input("\nEnter your state: ")
my_dict['state'] = state

# Final Dictionary
print("\n--- Final Dictionary ---")
for key, value in my_dict.items():
    print(f"{key} : {value}")
