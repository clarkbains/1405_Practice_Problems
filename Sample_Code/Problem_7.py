def promptForImput(query, typeInput):
    while True:
        userIn = input(query)
        if typeInput == "num":
            if userIn.isdigit():
                return userIn
        if typeInput == "any":
            return userIn
        print("Error: Input must be of type " + typeInput)


print("Please Select an option")
print("[1] - Add a course")
print("[2] - Drop a course")
choice = promptForImput("> ", "num")
choice = int(choice)
if choice == 1:
    print("Enter Course Name: ")
    course_name = promptForImput(">", "any")
    print("Enter Course ID: ")
    course_id = promptForImput(">", "any")
    print("Added " + course_name + ", course id is " + course_id)
if choice == 2:
    print("Enter Course Name: ")
    course_name = promptForImput(">", "any")
    print("Removed " + course_name + " from your course")
if choice < 1 or choice > 2:
    print("Bad Input")
