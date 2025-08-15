user_string=input("Enter A Name:")

for name in user_string:
    print(name)
    if user_string.lower().count(name)==1:
        print("Non Repeated Character Is :",name)
        break;
        
