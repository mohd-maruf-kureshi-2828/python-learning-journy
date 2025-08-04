userInt=int(input("Enter Number:"))
sum_even=0
for i in  range(1,userInt+1):
    if i%2==0:
        sum_even+=1

print("even numbers is",sum_even)