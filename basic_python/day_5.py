studentDetails={
    "name":"Maruf",
    "Depart":"Cs",
    "skill":"js"
    
}

# print(studentDetails["name"])
# getname=studentDetails.get("name")
# print(getname)

# studentDetails["name"]="mohamed maruf kureshi"
# print(studentDetails)

# for key,value in studentDetails.items():
#     print(f"key is {key}: value is {value}")

# for keys in studentDetails:
#     print(keys,studentDetails[keys])


# if "name" in studentDetails:
#     print("name key have in dic")


# print(len(studentDetails))


# added key value
studentDetails["Degre"]="BCA"
# print(studentDetails)

studentDetails.pop("Degre")
# print(studentDetails)

# list item remove karta hai
studentDetails.popitem()
# print(studentDetails)

# referece delete kar dita hai delete del() method
del studentDetails["Depart"]
# print(studentDetails)




#copy bana sakte hai using copy method
studentDetails_copy=studentDetails.copy()
# print(studentDetails) 


bcaStudents={
    "names":{
        "name1":"maruf",
        "name2":"arbaz"
    },
    "skills":{
        "skill1":"web dev",
        "skill2":"communication"
    }
}
# print(bcaStudents)
# print(bcaStudents["names"]["name1"])
for section in bcaStudents:
    print("category :" ,section)
    for key in bcaStudents[section]:
        print(key, ":",bcaStudents[section][key])


names=["maruf","kureshi"]
values="js"
newDict=dict.fromkeys(names,values)
print(newDict)