"""
user_int=int(input("Enter A Number To Print Your Msg:"))
for i in range(user_int):
    print("Maruf")
"""


"""
natural_number=int(input("Enter A Natural Number : "))
for i in range(1,natural_number+1):
    print(i)

"""


"""
user_input=int(input("Enter A Number For Reversing: "))
for i in range(user_input,0,-1):
    print(i,end=" ")
 """

"""
user_table=int(input("Enter A Number For A Table: "))
for i in range(1,11):
    print(f"{user_table} X {i} = {user_table*i}")
"""

"""
sum of number
user_sum=int(input("Enter A Number : "))
sum=0;
for i in range(1,user_sum+1):
    sum+=i
print(f"Your Sum Is {sum}")
"""


"""
user_fact=int(input("Enter A Number : "))
fact=1;
for i in range(1,user_fact+1):
    fact*=i
print(f"Factory Of A Number Is {fact}")
"""


"""
user_input=int(input("Enter A Number : "))
even=0
odd=0
for i in range(1,user_input+1):
    if(i%2) == 0:
        even+=i
    else:
        odd+=i
print(f"Your Even {even}, And Odd Is {odd}")    
"""
      
"""   
user_fact=int(input("which number factors you want : "))
for i in range(1,user_fact+1):
    if user_fact%i == 0:
        print(i)
"""


"""
find perfect number and factorial
number=int(input("Enter A Number : "))
sum=0
for i in range(1,number):
    if number%i == 0:
        sum+=i
if sum == number:
    print("perfect number")
else:
    print("Not A Perfect Number")
"""


"""
user_prime=int(input("Enter A Number To Check Prime : "))
count=0
for i in range(1,user_prime+1):
    if user_prime%i == 0:
        count += 1
if count == 2:
    print("Your Number Is Prime ")
else:
    print("Your Number Is Not Prime ")
"""


"""
user_str_rev=input("Enter Anything For Reversing : ")
reversed_str=""
for i in range(len(user_str_rev)-1,-1,-1):
    # print(user_str_rev[i],end=" ")
    reversed_str += user_str_rev[i]

if reversed_str == user_str_rev:
    print("Your String Is Palindrome")
else:
    print("Your String Is Not Palindrome")
"""

Counting=input("Enter A Number For Counting :")
char=0
num=0
special_char=0
for i in Counting:
    if i.isalpha():
        char += 1
    elif i.isdigit():
        num += 1
    else:
        special_char += 1

print(f"Your Chararcter Are {char}\nYour Number Are {num}\n Your Speacial Character Are {special_char}")
    