def my_decorator(func):
    def wrapper():

        print("Funtion ke start  me decoration")
        func()
        print("Funtion ke end me decoration")

    return wrapper

# @my_decorator
def say_hello_dev():
    print("Hello Python Leaner")

# say_hello_dev()


# decorator without @ symbol

def say_hey():
    print("Hello Python Leaner")

decorated=my_decorator(say_hey)
# decorated()


def Argument_decor(func):
    def wrapper(*args,**kwargms):
        print("Before Funtion Call")
        result=func(*args,**kwargms)
        print("After Funtion Call")
        return result
    return wrapper

@Argument_decor
def Sum(a,b):
    print(f"Additional Of Two Number {a} + {b}")
    return a + b

# obj=Sum(25,25)
# print(obj)


# multiple decorators
def decorator1(func):
    def wrapper(*args,**kwargs):
        print("Decorator 1 Start")
        func(*args,**kwargs)
        print("End Decorator 1")
    return wrapper

def decorator2(func):
    def wrapper(*args,**kwargs):
        print("Decorator 2 Star")
        func(*args,**kwargs)
        print("End Decorator 2" )
    return wrapper

@decorator1
@decorator2
def hello():
    print("Hello bhai")

# hello()



# Real Life Example – Authentication
def require_login(func):
    def wrapper(user):
        if user.lower() !="maruf":
            print("Access Denied 🚫")
        else:
            return func(user)
    return wrapper

@require_login
def dashboard(user):
    print(f"Welcome {user} to your dashboard 🤝")

dashboard("MARUF")

def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
           for i in range(n+1):
               func(*args,**kwargs)  
        return wrapper
    return decorator
@repeat(10)
def  names(name):
    print(f"{name} Hey Dude")

# names("maruf")
