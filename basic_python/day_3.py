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