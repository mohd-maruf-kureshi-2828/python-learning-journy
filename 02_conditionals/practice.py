"""
num1=int(input("Enter A First Number :"))
num2=int(input("Enter A Second Number :"))

if num1>num2:
    print(f"{num1} Is Greater Then {num2}")
elif num2>num1:
    print(f"{num2} Is Greater Then {num1}")
else:
    print("Both Number Are Same")
"""


"""
user_check=input("Enter Gender Male Or Female :")
if user_check=="Male" or user_check=="male":
    print("Good Morning sir")
elif user_check=="Female" or user_check=="female":
    print("Good Morning mam")
else:
    print("Enter A Gender Plz Try Again")
"""


"""
user_input=int(input("Enter A Number To Check Is Even Or Odd : "))

if (user_input%2) == 0:
    print(f"{user_input} Is A Even Number")
else:
    print(f"{user_input} Is A Odd Number")
"""


"""
Voter_name=input("Enter Your Name :")
Voter_age=int(input("Enter Your Age :"))

if Voter_age>=18:
    print(f"{Voter_name} Congraturation Your Valid For Vote")
elif Voter_age<18 :
    print(f"{Voter_name} Sorry Your Not Valid For Vote Because Your Age Is {Voter_age}")
else:
    print("Invalid Something")
"""


"""
user_check=int(input("Enter A Year To Check Is Leap Year Or Not : "))

if (user_check % 4 == 0) and(user_check % 100 !=0) or (user_check % 4==0):
    print(f"{user_check} It's A Leap Year")
else:
    print(f"{user_check} Its Not A Leap Year")
"""


user_temp=int(input("Enter A Temperature : "))
if user_temp<0:
    print("Freezing Cold 🥶")
elif user_temp>=0 and user_temp<10:
    print("Very Cold🤧")
elif user_temp>=10 and user_temp<20:
    print("Cold😷")
elif user_temp>=20 and user_temp<30:
    print("pleasant💬")
elif user_temp>=30 and user_temp<40:
    print("Hot 🔥")
else:
    print("Very Hot 🥵")