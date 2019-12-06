userDict = {}
def handleMsg (userDict, msg):
    outMessage = ""
    while True:
        print ("Looping", userDict['level'])
        if userDict['level'] == 0:
            outStr = "[1] - View Overall Grade\n[2] - Add Course\n\n[3] - Select A Course\n[4] - Remove Course"
            keysToDelete = []
            #for key in userDict:
            #    if key not in ['level', 'courses']:
            #        keysToDelete.append(key)
            #for key in keysToDelete:
            #    del userDict[key]
            promptForInput (outStr, userDict, 0.1)
            break
        if userDict['level'] == 0.1:
            if (msg.isdigit() and 0<int(msg)<5):
                selection = int(msg)
                if selection == 1:
                    advanceLevel (userDict, 2)
                elif selection == 2:
                    advanceLevel (userDict, 3)
                elif selection == 3:
                    advanceLevel (userDict, 4)
                elif selection == 4:
                    advanceLevel (userDict, 5)
            else:
                sayAndAdvance ("Bad Input.", userDict, userDict['lastlevel'])
                break
        if userDict['level'] == 2:
            sayAndAdvance ("Grade Is " + "95", userDict, 0)
            print (userDict)      
        if userDict['level'] == 3:
            promptForInput ("Course Name? ", userDict, 3.1)
            break
        if userDict['level'] == 3.1:
            if len(msg)>0:
                userDict['coursename'] = msg
                promptForInput ("Course Notes? ", userDict, 3.2)
                break
            else:
                sayAndAdvance ("Bad Input.", userDict, userDict['lastlevel'])
        if userDict['level'] == 3.2:
            
            userDict['coursenotes'] = msg
            if ('courses' not in userDict):
                userDict['courses'] = []
            skeletoncourse = {
                'name':userDict['coursename'],
                'notes': userDict['coursenotes']
            }
            userDict['courses'].append(skeletoncourse)
            sayAndAdvance ("Course Added? " + userDict['coursename'] + userDict['coursenotes'], userDict, 0)
        if userDict['level'] == 4:
            courses = listAndIndexCourses(userDict)
            promptForInput (courses, userDict, 4.1)
            break
        if userDict['level'] == 4.1:
            if (msg.isdigit() and 0<=int(msg)<len(userDict['courses'])):
                userDict['selectedcourse'] = int(msg)
                sayAndAdvance("Selected " + userDict['courses'][int(msg)]['name'], userDict, 4.2)
            else:
                sayAndAdvance ("Bad Input.", userDict, userDict['lastlevel'])
        if userDict['level'] == 4.2:
            menu = "[0] - view mark\n[1] - add grade\n[2] - see grades\n[3] - remove grade\nSelect an option"
            promptForInput(menu,userDict,4.3)
            break

        if userDict['level'] == 4.3:
            if (msg.isdigit() and 0<=int(msg)<3):
                selection = int(msg)
                if selection == 0:
                    advanceLevel (userDict, 4.31)
                elif selection == 1:
                    advanceLevel (userDict, 4.32)
                elif selection == 2:
                    advanceLevel (userDict, 4.33)
                elif selection == 3:
                    advanceLevel (userDict, 4.34)
            else:
                sayAndAdvance ("Bad Input.", userDict, userDict['lastlevel'])
                break
        if userDict['level'] == 4.31:
            if 'grades' not in userDict['courses'][userDict['selectedcourse']]:
                userDict['courses'][userDict['selectedcourse']]['grades'] = []
            earned = 0
            adjustedGrades = 0

            for grade in userDict['courses'][userDict['selectedcourse']]['grades']:
                earned += float(grade['weight'])
                adjustedGrades += float(grade['weight']) * float(grade['grade'])
            sayAndAdvance("Your Grade is " + str(adjustedGrades/earned), userDict, 0)
        if userDict['level'] == 4.32:
            promptForInput ("Grade Note ", userDict, 4.321)
            break
        if userDict['level'] == 4.321:
            if len(msg)>0:
                userDict['gradename'] = msg
                promptForInput ("Grade Weight? [0-100]", userDict, 4.322)
                break
            else:
                sayAndAdvance ("Bad Input.", userDict, userDict['lastlevel'])
        if userDict['level'] == 4.322:
            if len(msg)>0:
                userDict['gradeweight'] = float(msg)
                promptForInput ("Grade [0-100]? ", userDict, 4.323)
                break
            else:
                sayAndAdvance ("Bad Input.", userDict, userDict['lastlevel'])
        if userDict['level'] == 4.323:
            if len(msg)>0:
                userDict['gradeval'] = float(msg)
                advanceLevel (userDict, 4.323)
            else:
                sayAndAdvance ("Bad Input.", userDict, userDict['lastlevel'])
        if userDict['level'] == 4.323:
            skeletonGrade = {
                'note':userDict['gradename'],
                'weight':userDict['gradeweight'],
                'grade':userDict['gradeval'] 
            }
            if 'grades' not in userDict['courses'][userDict['selectedcourse']]:
                userDict['courses'][userDict['selectedcourse']]['grades'] = []
            userDict['courses'][userDict['selectedcourse']]['grades'].append(skeletonGrade)
            sayAndAdvance ("Added Grade: " + str(skeletonGrade), userDict,0)
        if userDict['level'] == 4.33:
            if 'grades' not in userDict['courses'][userDict['selectedcourse']]:
                userDict['courses'][userDict['selectedcourse']]['grades'] = []
            outVal = ""
            for grade in userDict['courses'][userDict['selectedcourse']]['grades']:
                outVal += "["+grade['note']+"], w:" + str(grade['weight']) + ", " + str(grade['grade']) + "%"
            sayAndAdvance(outVal, userDict, 4.1)
    return True

        



def listAndIndexCourses (userDict):
    outMessage = ""
    counter = 0
    for course in userDict['courses']:
        outMessage += "[" + str(counter) + "] " + course['name'] + ((" ("+course['notes']+ ")\n") if course['notes'] else "\n")
    return outMessage + "Select a course: "
def sayAndAdvance (msg, userDict, continueTo):
    promptForInput (msg, userDict, continueTo)

def promptForInput (msg, userDict, continueTo):
    advanceLevel(userDict, continueTo)
    if len(msg)>0:
        print (msg)

def advanceLevel (userDict, continueTo):
    userDict['lastlevel'] = userDict['level']
    userDict['level'] = continueTo


userID = input("Enter your Userid: ")
if userID not in userDict:
    userDict[userID] = {}
    userDict[userID]['level'] = 0 #Home Menu
    handleMsg(userDict[userID],"")

m = input ("Input: ")
while handleMsg(userDict[userID],m):
    m = input ("Input: ")
    