method= lambda num1,num2: print("Using Lamda Function Sum Of Two Nums",num1+num2)
method(1,2)
method(20,25)

User_names=lambda user_int1:print(f"Your Name IS {user_int1}")
User_names("maruf kureshi")


sql_of_num=lambda x:x**2
# print(sql_of_num(10))


# A lambda function that returns "Even" if the number is even, otherwise "Odd"
is_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"

# print(is_even_odd(4))  # Output: Even
# print(is_even_odd(7))  # Output: Odd



# Greaters Number
Greates_Number = lambda num1,num2:f"{num1} Great Then {num2}" if num1 > num2 else f"{num2} Great Then {num1}"
# print(Greates_Number(1,2))
# print(Greates_Number(20,10))


#valid for voting
User_valid=lambda age: f"Your Eligible For Vote {age}" if age>=18 else f"Your Not Eligible For Vote {age}"
user_result=User_valid(10)
# print(user_result)

# filter
My_list=[10,11,12,13,14,15]
method_lamda=list(filter(lambda i:(i%2!=0),My_list))

# method_mda=list(map(lambda i:(i%2!=0),My_list))
# print(method_mda)

Method_map=list(map(lambda x:x*2,My_list))
print(Method_map)


Names_list=["mauf","kureshi","arbaz"]
map_pract=list(map(lambda x:x.upper(),Names_list))
print(map_pract)


"""
for i in My_list:
    if i%2!=0:
        print(f"{i} Odd Number")
"""
