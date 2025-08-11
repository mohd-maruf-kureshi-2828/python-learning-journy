"""
emty_list=[]
for i in range(1,11):
    user_input=int(input("Enter A Number :"))
    emty_list.append(user_input)
    if user_input>0:
        # positive_number+=1
        print("positive numbers is",user_input)
    

"""

empt_list=[]
positive_number=0
for i in range(1,5):
    user_input=int(input("Enter A Number : "))
    empt_list.append(user_input)
    if user_input>0:
        positive_number+=1

print("Total Positive Numbers Is",positive_number)
