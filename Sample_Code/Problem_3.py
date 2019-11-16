print ("Please Select an option")
print ("[1] - Add a course")
print ("[2] - Drop a course")
print ("[3] - Edit a grade")
optionL1 = input ("option: ")
optionAsNumL1 = int(optionL1)

if optionAsNumL1 == 1:
    courseName = input ("What is the name of this course to add? ")
    courseId = input ("What is the id of this course? ")
elif optionAsNumL1 == 2:
    courseName = input ("What is the name of this course to remove? ")
elif optionAsNumL1 == 3:
    optionL2 = input ("Please Select a course: ")
    courseName = int(optionL2)
    print ("Please Select an option")
    print ("[1] - Add a Grade")
    print ("[2] - Drop a Grade")
    print ("[3] - Edit a Grade")
    optionL3 = input ("option: ")
    optionAsNumL3 = int(optionL3)
    if optionAsNumL3 == 1:
        grade_weight = float(input ("What is the weight of the grade? [0.00-1.00] "))
        grade_val = float(input ("What is the grade? [0.00-1.00] "))
    elif optionAsNumL3 == 2:
        print ("Pick the grade you want to remove: ")
        print ("*List Grades here*")
        optionL4 = input ("Grade: ")
        optionAsNumL4 = int(optionL4) 
    elif optionAsNumL3 == 3:
        print ("Pick the grade you want to edit: ")
        print ("*List Grades here*")
        optionL4 = input ("Grade: ")
        optionAsNumL4 = int(optionL4)
        new_mark = float(input ("New grade is: "))
        new_weight = float(input ("New weight is: "))

if optionAsNumL1 == 1:
    print ("You have added " + courseName + ", course id " + courseId + ".")
elif optionAsNumL1 == 2:
    courseName = input ("What is the name of this course ot remove? ")
elif optionAsNumL1 == 3:
    optionL2 = input ("Please Select a course: ")
    courseName = int(optionL2)
    print ("Please Select an option")
    print ("[1] - Add a Grade")
    print ("[2] - Drop a Grade")
    print ("[3] - Edit a Grade")
    optionL3 = input ("option: ")
    optionAsNumL3 = int(optionL3)
    if optionAsNumL3 == 1:
        grade_weight = float(input ("What is the weight of the grade? [0.00-1.00] "))
        grade_val = float(input ("What is the grade? [0.00-1.00] "))
        print ()
    elif optionAsNumL3 == 2:
        print ("Pick the grade you want to remove: ")
        print ("*List Grades here*")
        optionL4 = input ("Grade: ")
        optionAsNumL4 = int(optionL4) 
    elif optionAsNumL3 == 3:
        print ("Pick the grade you want to edit: ")
        print ("*List Grades here*")
        optionL4 = input ("Grade: ")
        optionAsNumL4 = int(optionL4)
        new_mark = float(input ("New grade is: "))
        new_weight = float(input ("New weight is: "))



