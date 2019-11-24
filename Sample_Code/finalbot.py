userDict = {}
import discord
import json

client = discord.Client()
def readData (file):
    global userDict
    f = open (file, 'r')
    userDict = json.load(f)
    f.close()

def writeData (file):
    f = open (file, 'w')
    json.dump(userDict, f)
    f.close()
def readConfig (file):
    d = {}
    f = open (file, 'r')
    for l in f:
        inConfig = l.split(",")
        if len(inConfig) >= 2:
            d[inConfig[0]] = inConfig[1]
    f.close()
    return d

async def handleMsg (userDict, msg, channel):
    while True:
        print ("Looping", userDict['level'])
        if userDict['level'] == 0:
            outStr = "[1] - View Overall Grade\n[2] - Add Course\n[3] - Select A Course\n[4] - Remove Course"
            await promptForInput (outStr, userDict, 0.1, channel)
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
                await sayAndAdvance ("Bad Input.", userDict, userDict['lastlevel'],channel)
                break
        if userDict['level'] == 2:
            total = 0
            num = 0
            for course in userDict['courses']:
                grade = calculateCourseGrade(course)
                if grade != -1:
                    total += grade
                    num +=1
            if num == 0:
                await sayAndAdvance("Your Grade cannot be calculated right now.", userDict, 4.2,channel)
            else:
                await sayAndAdvance("Your Grade is " + str(total/num), userDict, 4.2,channel)
            print (userDict)      
        if userDict['level'] == 3:
            await promptForInput ("Course Name? ", userDict, 3.1, channel)
            break
        if userDict['level'] == 3.1:
            if len(msg)>0:
                userDict['coursename'] = msg
                await promptForInput ("Course Notes? ", userDict, 3.2,channel)
                break
            else:
                await sayAndAdvance ("Bad Input.", userDict, userDict['lastlevel'], channel)
        if userDict['level'] == 3.2:
            
            userDict['coursenotes'] = msg
            if ('courses' not in userDict):
                userDict['courses'] = []
            skeletoncourse = {
                'name':userDict['coursename'],
                'notes': userDict['coursenotes']
            }
            userDict['courses'].append(skeletoncourse)
            await sayAndAdvance ("Course Added? " + userDict['coursename'] + userDict['coursenotes'], userDict, 0,channel)
        if userDict['level'] == 5:
            courses = listAndIndexCourses(userDict)
            await promptForInput (courses, userDict, 5.1, channel)
            break
        if userDict['level'] == 5.1:
            if (msg.isdigit() and 0<=int(msg)<len(userDict['courses'])):
                userDict['courses'].pop(int(msg))
                await sayAndAdvance ("Removed Course", userDict, 0, channel)
            else:
                await sayAndAdvance ("Bad Input.", userDict, userDict['lastlevel'],channel)
        if userDict['level'] == 4:
            courses = listAndIndexCourses(userDict)
            await promptForInput (courses, userDict, 4.1, channel)
            break
        if userDict['level'] == 4.1:
            if 'courses' in userDict and msg.isdigit() and 0<=int(msg)<len(userDict['courses']) and msg != "":
                userDict['selectedcourse'] = int(msg)
                await sayAndAdvance("Selected " + userDict['courses'][int(msg)]['name'], userDict, 4.2, channel)
            else:
                await sayAndAdvance ("Bad Input.", userDict, userDict['lastlevel'],channel)
        if userDict['level'] == 4.2:
            menu = "[0] - view mark\n[1] - add grade\n[2] - see grades\n[3] - remove grade\nSelect an option"
            await promptForInput(menu,userDict,4.3,channel)
            break

        if userDict['level'] == 4.3:
            if (msg.isdigit() and 0<=int(msg)<4):
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
                await sayAndAdvance ("Bad Input.", userDict, userDict['lastlevel'],channel)
                break
        if userDict['level'] == 4.31:
            grade = calculateCourseGrade(userDict['courses'][userDict['selectedcourse']])
            if grade == -1:
                await sayAndAdvance("Your Grade cannot be calculated right now.", userDict, 4.2,channel)
            else:
                await sayAndAdvance("Your Grade is " + str(grade), userDict, 4.2,channel)
        if userDict['level'] == 4.32:
            await promptForInput ("Grade Note ", userDict, 4.321,channel)
            break
        if userDict['level'] == 4.321:
            if len(msg)>0:
                userDict['gradename'] = msg
                await promptForInput ("Grade Weight? [0-100]", userDict, 4.322,channel)
                break
            else:
                await sayAndAdvance ("Bad Input.", userDict, userDict['lastlevel'],channel)
        if userDict['level'] == 4.322:
            if len(msg)>0:
                userDict['gradeweight'] = float(msg)
                await promptForInput ("Grade [0-100]? ", userDict, 4.323,channel)
                break
            else:
                await sayAndAdvance ("Bad Input.", userDict, userDict['lastlevel'],channel)
        if userDict['level'] == 4.323:
            if len(msg)>0:
                userDict['gradeval'] = float(msg)
                advanceLevel (userDict, 4.324)
            else:
                await sayAndAdvance ("Bad Input.", userDict, userDict['lastlevel'],channel)
        if userDict['level'] == 4.324:
            skeletonGrade = {
                'note':userDict['gradename'],
                'weight':userDict['gradeweight'],
                'grade':userDict['gradeval'] 
            }
            if 'grades' not in userDict['courses'][userDict['selectedcourse']]:
                userDict['courses'][userDict['selectedcourse']]['grades'] = []
            userDict['courses'][userDict['selectedcourse']]['grades'].append(skeletonGrade)
            await sayAndAdvance ("Added Grade: " + skeletonGrade['note'], userDict,4.2,channel)
        if userDict['level'] == 4.33:
            await sayAndAdvance(listAndIndexGrades(userDict['courses'][userDict['selectedcourse']]),userDict,4.2,channel)
        if userDict['level'] == 4.34:
            gradeList = "Select a grade:\n" + listAndIndexGrades(userDict['courses'][userDict['selectedcourse']])
            await promptForInput(gradeList,userDict,4.35,channel)
            break
        if userDict['level'] == 4.35:
            if msg.isdigit() and 0<=int(msg)<len(userDict['courses'][userDict['selectedcourse']]) and msg != "":
                userDict['courses'][userDict['selectedcourse']].pop (int(msg))
                await sayAndAdvance("Removed Grade",userDict,4.2,channel)
            else:
                await sayAndAdvance ("Bad Input.", userDict, userDict['lastlevel'],channel)
           
           
            
def calculateCourseGrade (gradeDic):
    if 'grades' not in gradeDic:
        gradeDic['grades'] = []
    earned = 0
    adjustedGrades = 0
    for grade in gradeDic['grades']:
        earned += float(grade['weight'])
        adjustedGrades += float(grade['weight']) * float(grade['grade'])
    if earned == 0:
        return -1
    return adjustedGrades/earned        

def listAndIndexGrades (gradeDic):
    if 'grades' not in gradeDic:
        gradeDic['grades'] = []
    outVal = ""
    counter = 0
    for grade in gradeDic['grades']:
        outVal += "["+str(counter)+"] " + "("+grade['note']+"), w:" + str(grade['weight']) + ", " + str(grade['grade']) + "%\n"
        counter +=1
    if len(outVal)==0:
        return "No Grades"
    else:
        return outVal
def listAndIndexCourses (userDict):
    outMessage = ""
    counter = 0
    if 'courses' in userDict:
        for course in userDict['courses']:
            outMessage += "[" + str(counter) + "] " + course['name'] + ((" ("+course['notes']+ ")\n") if course['notes'] else "\n")
            counter +=1
        return outMessage + "Select a course: "
    return "`;;~` to go home. No Courses Found"
async def sayAndAdvance (msg, userDict, continueTo,channel):
    await promptForInput (msg, userDict, continueTo, channel)

async def promptForInput (msg, userDict, continueTo, channel):
    advanceLevel(userDict, continueTo)
    if len(msg)>0:
        print (msg)
        await channel.send(msg)

def advanceLevel (userDict, continueTo):
    userDict['lastlevel'] = userDict['level']
    userDict['level'] = continueTo


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(';;'):
        if str(message.author) not in userDict:
            userDict[str(message.author)] = {}
            userDict[str(message.author)]['level'] = 0 #Home Menu
        if message.content == ";;~":
            userDict[str(message.author)]['level'] = 0
            message.content == ";;" 
        await handleMsg(userDict[str(message.author)],message.content[2:],message.channel)
        writeData("d")
opts = readConfig("auth")
readData("d")
client.run(opts['apikey'])
