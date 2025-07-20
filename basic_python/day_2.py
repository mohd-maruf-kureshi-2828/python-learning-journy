"""operator in python

1 Arthmetic operator
+, * , / , - , % , // , **.

2 Assigment operator
= , += , == , -= , *= , /= , //= , **=.

3 Comparison operator
== , <= , >= , < , >

4 logical operator
and , or , not

5 Bitwise operator
& , | , ^ , ~ , << , >> 

"""

# 1 Arthmetic operator
"""
a=20
b=10

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

"""

"""
2 Assigment operator
a=10
# a=10+1
a+=10
print("a+=10",a)
a-=10
print("a-=10",a)
a*=10
print("a*=10",a)
a**=10
print("a**=10",a)
a/=10
print("a/=10",a)
a//=10
print("a//=10",a)
"""

"""
3 comaparison operator
a=10
b=20
print(a>b)
print(a<b)
print(a==b)
print(a>=b)
print(a<=b)
"""


"""
4 logical operator
a=10
b=25
print(a<b and b>a) and operator its returns true when both condition is true
print(a>b and b>a)

print(a<b or b>a)any one condition is true its return the value true
print(a>b or b>a)

print(a<b != b>a) if condition is true  return the value is false
"""

# 5 bitwise operator

a=5
b=6

# how its work
"""
& operator work flow
8 4 2 1  
0 1 0 1
0 1 1 0   
0 1 0 0 = 4
"""
print(a&b)

"""
| operator work flow
8 4 2 1
0 1 0 1
0 1 1 0
0 1 1 1 = 7
"""
print(a|b)

"""
^ operator
8 4 2 1
0 1 0 1
0 1 1 0
0 0 1 1 = 3
"""
print(a^b)

"""
how its work me see here 
a=5 
~(a)
~(5)
~(5+1)
-(+6) =-+=-
(-6)
  """
print(~a)


"""
<< left shift
a = 5
 here we see how its work and the out put is 10 here the left we give only 1 step
    8 4 2 1
    0 1 0 1 
  0 1 0 1
    10
"""
print(a<<1)

"""
>> right shift
a= 5
    8 4 2 1
    0 1 0 1 
      0 1 0 1
       2

"""
print(a>>1)