print ("Please Select an option")
print ("[1] - Add a course")
print ("[2] - Drop a course")
option = input ("option: ")
optionAsNum = int(option)
if optionAsNum == 1:
    courseName = input ("What is the name of this course to add? ")
    courseId = input ("What is the id of this course? ")
    outMsg = "Added " + courseName + ", course id is " + courseId + "."
    print (outMsg)
if optionAsNum == 2:
    courseName = input ("What is the name of this course ot remove? ")
    outMsg = "Removed " + courseName + " from your courses."
    print (outMsg)