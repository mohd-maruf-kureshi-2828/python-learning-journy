"""
data types in python
1 Numeric data types
  * int 1234
  * float 1.5
  * bool true or false
  * complex 5j

2 sequential data types
   * list []
   * tuple ()
   * set {}
   * dict {key : value}
   * range
   * str
"""

"""
list
marks=[75,89,23,30,60]
names=["maruf","kureshi","arbaz"]
print(type (marks))
print(marks)
marks.append(29)
print(marks)

print(marks[1])
marks[1]=23
print(marks)

print(marks[0:2])

add=[*marks,*names]
print(add)

nest=[[1,2],[4,5],[9,10]]
print(*nest[0],*nest[1],*nest[2])
"""
newList=[1,2,3,4,5]
newList.insert(2,"hello")
newList.remove("hello")
newList.reverse()
newList.extend("hey")
print(newList)


# 08class for revision

# li1=[1,2,3,4,5,[70]]
# li2=[6,7,8,9]
# li1.extend(li2)
# l3=li1+li2
# print(l3)
# li1.extend(li1)
# li1.extend()
# print(li1[5])

# li1=[1,2,3,4,5]
# li2=[6,7,8,9]
# li1.extend(l2) only for sequential data type
# print(li1)

# l1=[10,20]
# any="hello"
# l1.append(any)
# print(l1)
li1=[10,20,30,40,50]
# li1.insert(2,400)
# li1.reverse()
# li1.sort()
# li1.remove(10)
# li1.pop(2)
# print(li1)

# emptylist=[]
# li=[1,2,3,4,5]
# emptylist.append(li)
# print(emptylist)

# method2emp=[]
# userint=input("Enter Your Name :")
# method2emp.append(userint)
# print(method2emp)


"""
emptyList=[]
for item in range(5):
    name=input("enter your 5 names:")
    emptyList.append(name)

print("final 5 name",emptyList)
"""


"""
emptyList=[]
for item in range(10):
    name=int(input("Enter 10 numbers:"))
    emptyList.append(name)

print("final 10 numbers",emptyList)
"""


# list1=[1,2,3,4,5]
# print(list1)
# userAsk=int(input("Which position DO You Want to delete:"))
# list1.remove(userAsk)
# print(list1)


# list1=[10,20,30,40,50]
# userAsk=int(input("enter your numbers to append:"))
# list1.append(userAsk)
# print(list1)


list1=[10,20,30,40,50]
pos=int(input("enter your pos:"))
if pos in range(len(list1)):
    ele=int(input("enter your element"))
    list1.insert(pos,ele)
    print("final list",list1)
else:
    print("invalid input")


# tuple is unmutuable
"""
name=("maruf","kureshi","maruf")
print(type(name))
print(name)

number=(20,1,15,40,2)
print(number)
state=("Gujarat","karnata","maharashtra")
lang=("gujarati","kannada","marathi")
add=state+lang
print(add)
"""
"""
numbers=(1,2,4,2,8,9,2,6,3)
print(numbers.count(2))
print(numbers.index(2))
"""

