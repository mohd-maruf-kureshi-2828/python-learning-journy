user_input=int(input("Enter A Number To check Prime Number : "))
is_prime=True
if user_input>1:
    for i in range(2,user_input):
        if (user_input%i)==0:
            is_prime=False
            break;
print(user_input,"is a prime")