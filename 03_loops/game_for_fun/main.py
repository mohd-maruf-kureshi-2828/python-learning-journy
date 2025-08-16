import random

User_Random=random.randint(1,100)
User_Try=0

while True:
    User_input=int(input("Enter A Number b/t 1 to 100 : "))

    if User_input == User_Random:
        print(f"Your Guess The Right Number {User_input}")
        User_Try += 1
        break;
    elif User_input > User_Random:
        print(f"Your Guessing The Number Is Greaten {User_input}")
        User_Try +=1
    else:
         print(f"Your Guessing The Number Is Less {User_input}")
    