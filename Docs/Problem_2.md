# Practice problem 2
Programmers can only get so far by asking for input and regurgitating it a few seconds later. This problem tracks as you add some logic into the bot.

The user should be presented a menu, of which they can chose a command. Once they've chosen a command, it should ask for any additional input. Keeping on theme with the grade bot, here are the two commands it should accept.
```
[1] - Add a course
[2] - Drop a course
```
* `[1] - Add a course` should ask for the course name, and course code. After asking, it should print out a statement saying `Added {course_name}, course id is {course_id}`

* `[2] - Drop a course` should say `Removed {course_name} from your courses`
---
Syntax to know:
* `if` allows your program to be a little smart. If the `{statement}` is true, then the `{do this}` code will be run. Note that is must be indented in a similar fashion to below.
```
if {statement}:
        {do this}
```
* `==` allows you to test for equality. it evaluates to true if the value on the right is equal to the value on the left. Note that the inputs must be the same type. (int and int, str*ing* and str*ing*)

