"""
1 problem
userInt=int(input("Enter a number: "))
if userInt % 2==0:
    print(userInt,"even number")
else:
    print(userInt,"odd number")
"""


""""
problem 2
userInt=float(input("Enter a temperature in celsius: "))
fahreheit=(userInt * 9/5)+32
print("temperature in fahrenheit:", fahreheit)
"""


"""
problem 3
def calculator_fact(n):
    result=1
    for i in range(1,n+1):
        result *=i
    return result
num=int(input("Enter a non negative number: "))
print("factorial is",calculator_fact(num))
"""

"""
problem 4
def sum_list_elements(numbers):
    total=0
    for num in numbers:
        total+=num
    return total
myList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(sum_list_elements(myList))
"""

"""
problem 5
def reverse_string(s):
    reversed_str=""
    for char in s:
        reversed_str+=char+reversed_str
    return reversed_str
userType=input("Enter a type of user: ")
print("reverse string is",reverse_string(userType))
"""


"""
problem 6

def count_msg(text):
    vowels="aeiou"
    count=0
    for char in text.lower():
        if char in vowels:
            count+=1
    return count
message=input("Enter a message: ")
print("Number of vowels is",count_msg(message))
"""

"""
problem 7
def find_max(numbers):
    maximum=0
    for num in numbers:
        if num>maximum:
            maximum=num
    return maximum
myList=[4,2,1,6,8,9]
print("maximum is",find_max(myList))
"""

"""
problem 8
def calculator(num1,num2):
    print(num1+num2)
    print(num1-num2)
    print(num1*num2)
    print(num1/num2)

userInt=int(input("Enter A First Number: "))
userType=int(input("Enter A Second Number: "))
print("calcucator of two number",calculator(userInt,userType))
"""




userName=input("Enter your name: ")
userPassword=input("Enter your password: ")
if userName=="Maruf" and userPassword=="maruf@124":
    print("Login Successful")
else:
    print("Login Failed")