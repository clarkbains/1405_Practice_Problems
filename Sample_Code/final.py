#This is a WIP final script for the bot. Hopefully writing this will make the steps to reach this more clear
students = {}
def loadCreds (filename):
    f = open (filename, 'r')
    opts = {}
    for line in f:
        pair = line.strip().split("::")
        opts[pair[0]] = pair[1]
    f.close()
    return opts
def getStudent(id):
    return students[id]
def generateCourseListForStudent(id):
        retVal = ""
        currStudent = getStudent(id)
        if len(currStudent["courses"]):
            for idex in range(len(currStudent["courses"])):
                retval += "[" + str(idex) + "] - " + currStudent["courses"][idex]
        else:
            retVal = "You have no courses. Run `;;courses add [course_name]` to add"
        return retVal

def addCourse (id, courseName):
    if "grades" not in students[id] or "courses" not in students[id]:
        students[id] = {}
        students[id]["courses"] = []
        students[id]["grades"] = {}
    if courseName in students[id]["courses"]:
        return "You already have that course"
    students[id]["courses"].append(courseName)
    students[id]["grades"][courseName] = []
    return "You now have course " + courseName + " "
    
