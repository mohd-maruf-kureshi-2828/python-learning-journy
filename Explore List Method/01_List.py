Empty_list=[]
"""
for i in range(10):
    Enter_BY_User=int(input("Enter A Number"))
    Empty_list.append(Enter_BY_User)

print(Empty_list)
"""


"""
My_List=[10,20,30,40,50]
print(My_List)
User_position=int(input("Enter A Position : "))
User_Element=input("Enter A Element To Insert :")
if 0<=User_position<=len(My_List):
    My_List.insert(User_position,User_Element)
else:
    print("INVALID POSITION")

print(My_List)
"""


"""
My_List=[10,20,30,40,50]
print(My_List)
User_value=int(input("Enter A Value To Delete :"))
if User_value in My_List:
     remove_value=My_List.remove(User_value)
     print(f"Removing ELement IS {User_value}")
else:
     print("INVALID ELEMENT")
print(My_List)
"""


"""
My_list=[10,20,30,40,50]
print(My_list)
User_delete=int(input("Enter A Position U Want To Delete"))
if 0<=User_delete<=len(My_list):
    deleted_pos=My_list.pop(User_delete)
    print(f"Deleted Element {deleted_pos}")
    print(f"List AFter Deleting By Position {My_list}")
else:
    print("INVALID POSITION")
"""

My_list=[10,20,30,40,50]
print(My_list)
User_find=int(input("Enter A Element To Find :"))
if User_find in My_list:
    print(f"Element Find At Index : {My_list.index(User_find)}")
else:
    print("-1")