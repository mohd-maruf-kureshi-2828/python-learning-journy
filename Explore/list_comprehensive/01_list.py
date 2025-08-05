"""
numbers=[]
for i in range(5):
    numbers.append(i)
print(numbers)

numbers=[i for i in range(5)]
print(numbers)
"""

"""
syntax of list comprehension
[expression for item ib iterable if condition]
"""

even=[i for i in range(1,10) if i%2==0]
# print(even)

odd=[i for i in range(1,10) if i%2!=0]
# print(odd)

squares=[i*i for i in range(1,6)]
# print(squares)

name="Maruf"
vowels=[ch for ch in name if ch in "aeiou"]
# print(vowels)

result=["even" if i%2==0 else "odd" for i in range(1,6)]
# print(result)

squares_result=[i*i for i in range(1,10) if i%2==0]
# print(squares_result)

pairs=[(x,y) for x in[1,2] for y in [3,4]]
# print(pairs)

language=["python","c++","js","ruby"]
"""
for word in language:
    upper_case=word.upper()
    print(upper_case)
"""
upper_case=[word.upper() for word in language]
# print(upper_case)
