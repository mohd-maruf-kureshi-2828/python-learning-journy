"""
def mypass():
    pass
mypass
"""

# keyword funtion
def courses(course1,course2,course3):
    print(f"course1={course1},course2={course2},course3={course3}")
    
# courses("bca","bcom","bba")
# courses("ca","bcom") ERROR
# courses(course1="bca",course2="bcom",course3="bba")
# courses(course1="bca",course2="bcom","bba") ERROR


# default function
def student_Details(name,age,language="English"):
    print(f"student name is {name} , student age is {age} , student now this language {language}")

# student_Details("maruf",12)
# student_Details("kureshi",26,"kannada") kannada aye ga language me 


# arbitrary parameters iska data type tuple hota hai
def students(*names):
    print(f"all students names= {names}")

# students("maruf","kureshi","umair","arbaz","jayashwanth","vijay kumar")


# sample
def details(name,skills,*role):
    print(f"Employe name is {name}, Employee skill is {skills}, and role of the Employee {role}")

# details("maruf kureshi","HTML CSS Boostrap Tailwind JS React Python Full Stack","Developer")4




# keyword arbitrary parameters
# data type dictionary
def My_Dict(**keys):
    for key,value in keys.items():
        print(f"{key}={value}")

# My_Dict(Name="Mohd Maruf Kureshi",Course="BCA", Skill="JS Python",Experience="Fresher")

