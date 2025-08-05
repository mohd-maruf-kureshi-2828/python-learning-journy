My_list=[]
for i in range(10):
    User_Input=int(input("Enter A Number"))
    My_list.append(User_Input)

My_tuple=tuple(My_list)
# print(My_tuple)
Find_element=input("Enter A ELement :")
if Find_element in My_tuple:
    print("The Element Found At Index",My_tuple(Find_element))
else:
    print("Invalid Index")