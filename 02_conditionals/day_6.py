""""
userAge=int(input("Enter Your Age 😉:"))

if userAge<13:
    print(f"{userAge} go to the school,child")
elif userAge<=19:
    print(f"{userAge} teenager" )
elif userAge<=59:
    print(f"{userAge} Adult")
else:
    print(f"{userAge} senior")

"""



"""
print("Ticket Booking 🚂")
age=int(input("Enter Your Age😀:"))
day=input("Enter The Day⛅ ?:").lower()
price = 12000 if age >= 18 else 10000
dis=2
discountAmount=(dis/100)*price
finalPrice = price - discountAmount
if age>=18 and day=="wednesday":
    print(f"Your age is {age} and your price is {price} and you get discount 2% {finalPrice}")
elif age<=18 and day=="wednesday":
    print(f"Your age is {age} and your price is {price} you get discount 2% {finalPrice}")
if age>=18 and day!="wednesday":
    print(f"Your Price is {price} you dont get discount because today is not wednesday ")
if age<=18 and day!="wednesday":
    print(f"Your Price is {price} you dont get discount because today is not wednesday ")
"""


"""
# Grade System 📚 
studentMarks = int(input("Enter Your Marks: "))
if studentMarks >=101:
    print("Invalid Marks")
    exit()

if studentMarks >= 90:
    print("Grade A")
elif studentMarks >= 80:
    print("Grade B")
elif studentMarks >= 70:
    print("Grade C")
elif studentMarks >= 60:
    print("Grade D")
else:
    print("Grade F")
"""


"""
fruit = input("Enter a fruit name: ").lower()
if fruit == "apple":
    print(f"{fruit} is red.")
elif fruit== "mongo":
    print(f"{fruit} yellow")
elif fruit=="pineapple":
    print(f"{fruit} yellow")
elif fruit=="grapes":
    print(f"{fruit} purple")
elif fruit=="watermelon":
    print(f"{fruit} green")
"""


"""
print("suggest best activity according to weather☁️")
enterWearther=input("Weather ☁️?:").lower()
if enterWearther =="sunny":
    print("Go for a walk🚶")
elif enterWearther =="rainy":
    print("Read a book📖")
elif enterWearther=="snowy":
    print("Build a snowman⛷️")
else:
    print("Your Not a Human")
"""


"""
transportSpeed=int(input("Enter Your Distance :"))
if transportSpeed <=3 :
    transt="walk🚶‍♂️"
elif transportSpeed<=15 :
    transt="Bike🚵"
else:
    transt="car🚓"

print(transt)
"""


"""
userPassword=input("enter a password :")
if len(userPassword)<6:
    print("weak password👎")
elif len(userPassword)<=10:
    print("password is medium")
else:
    print("password is strong 💪")
"""


"""
year=int(input("Enter year📅:"))
if (year%400==0) or (year%4==0 and year%100 !=0 ):
    print(year,"is a leap year")
else:
    print(year,"is NOT a leap year")
"""



print("Checking Your cat or dog foog category")
petName=input("Which One You have Cat Or Dog :").lower()
petAge=int(input("Enter Your Pet Age And Find There Food Category:"))
if petName == "dog" and petAge<=2:
    print("puppy food")
elif petName == "dog" and petAge>=2:
    print("Adult food")
elif petName == "cat" and petAge<=1:
    print("kitten food")
elif petName =="cat" and petAge>=1:
    print("Adult food")
else:
    print("please enter valid pet name or age")