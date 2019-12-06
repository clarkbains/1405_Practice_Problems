# Practice problem 8

For this task, you will need to restructure your bot code into a format where the discord bot will be able to save the current response it got, and the next response it needs to prompt for.

You will need to implement this first off using a dictionary to get the state, responses, and any other information you may need as soon as you receive a command from the user. Within this, you need to create a key to store the id of the next question to ask or information to display. This will also be easier if you store the initial option the user picked as another key/value pair in the user dictionary. Every piece of information you collect from the 'top level menu' to the final output should be stored in the user dictionary so that in the final stage the information is available to do the required steps with.

There should only be one or two `input` statements, as your bot will not have a way on discord to get a reply, but will only be able to get the text of the reply, and the user id. Below is a sample dictionary holding the information of a user at different states. You may use this or create your own method for storing user data. 

At the initial Menu. This would be the value for the key of the users id. 

```{'level': 0}```

After selecting option 1, add a course

```{'level': 1}```

After entering a course name

```{'level': 1.1, 'coursename': 'Test Course'}```

After entering a course note

```{'level': 1.2, 'coursename': 'Test Course', 'coursenote': 'Test Course Note'}```

After processing the above data

```{'level': 0, 'courses': [{'name': 'Test Course', 'notes': 'Test Course Note', 'grades': []}]}```

This is easiest achieved if you define a function, and provide it the user data, and the incoming message. Have a bunch of if statements for each different menu level. Store the message/modify the user data if need be, then print what is required, (will be changed to sending later), and then exit the function. The next time the user provides input, you can use the value of the level key to go to the right code, and run it with the message data you now have. An easy way to do this flow is to infinitely loop through the collection of if statements and break every time a user is prompted for input. Otherwise, just set set the level value, and in the next loop, the appropriate message will be printed, until eventually it prompts for input and exits the loop, Below is so pseduo code that resembles the structure
```
function menu (userid, userdic, msg)
    while true
        if userdic['level'] == 0
            print menu
            print message prompting for input
            userdic['level'] = 1
            break
        if userdic['level'] == 1
            if msg does not make sense
                print message bad
                userdic['level'] = 0
            if msg good
                print selected item #
                print enter text
                userdic['level'] = 2
                break
        ... And so on
```