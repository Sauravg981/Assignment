student = {
    "Saurav":99,
    "Rajat":65,
    "Alice":43
           }
name= input("Enter Student's Name: ")
if name in student:
    S_name = student[name]
    print("{}'s marks: " .format(name),S_name)
else:
    print("Student Not Found")
