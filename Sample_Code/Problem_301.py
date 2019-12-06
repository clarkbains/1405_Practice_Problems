while True:
    print ("Please Select an option. Q to Quit")
    print ("[1] - Add a course")
    print ("[2] - Drop a course")
    choice = input ("> ")
    if choice == 'q' or choice == 'Q':
        break
    choice = int(choice)
    if choice == 1:
        print ("Enter Course Name: ")
        course_name = input(">")
        print ("Enter Course ID: ")
        course_id = input(">")
        print ("Added " + course_name + ", course id is " + course_id)
    if choice == 2:
        print ("Enter Course Name: ")
        course_name = input(">")
        print ("Removed " + course_name + " from your course")
    if choice < 1 or choice > 2:
        print ("Bad Input")