li=[10,20,30,40]
my_iter = iter(li)
"""
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
"""

def generate_million_numbers():
    for i in range(1,100000,2):
        yield i
my_generator = generate_million_numbers()
print(next(my_generator))
print(next(my_generator))