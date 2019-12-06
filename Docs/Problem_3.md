# Practice problem 2
Programmers can only get so far by asking for input and regurgitating it a few seconds later. This problem tracks as you add some logic into the bot.

The user should be presented a menu, of which they can chose a command. Once they've chosen a command, it should ask for any additional input. Keeping on theme with the grade bot, here are the two commands it should accept.
```
[1] - Add a course
[2] - Drop a course
```
* `[1] - Add a course` should ask for the course name, and course code. After asking, it should print out a statement saying `Added {course_name}, course id is {course_id}`

* `[2] - Drop a course` should say `Removed {course_name} from your courses`
  
An invalid input number should print out a message, and exit. This program does not need to loop

---
Syntax to know:
* `if` allows your program to be a little smart. If the condition is true, then the `{do this}` code will be run. Note that is must be indented in a similar fashion to below.
```
if condition:
        {do this}
```
* You may use all the comparison operators from the last practice problem

[Conditional Reference](https://www.python-course.eu/python3_conditional_statements.php)