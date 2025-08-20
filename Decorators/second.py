def message(display):
    def message1():
        print("Good Morning")
        display()
        print("thank you")
    return message1()


@message
def display():
    print("Python Developer : Arbaz")


def login(admin):
    def user_login():
        print("Login Successful")
        admin()
    return user_login()

@login
def admin():
    print("Admin Login")