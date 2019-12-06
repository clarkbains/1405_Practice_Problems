inital = input ("Would you like to init with a [d]ictionary or [l]ist?")
if inital == "d":
    obj = {}
if inital == "l":
    obj = []
while True:
    choice = input ("Would you like to [a]dd something, or [p]rint and exit?")
    if choice == 'a':
        value = input ("Enter the value: ")
        if type(obj) == dict:
            key = input("You also have to enter the key: ")
            obj[key] = value
        else:
            obj.append(value)
    elif choice == 'p':
        if type(obj) == dict:
            for key in obj:
                print ("Key is: " + key + ", value is " + obj[key])
        else:
            for i in range(len(obj)):
                print ("[" + str(i) +"] : " + obj[i])
        break

    else:
        print ("Sorry, I didn't quite get that")
