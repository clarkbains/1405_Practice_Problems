# Practice problem 1
This task tracks as you create a basic greeter for the bot. A user should be able to input their name, and have it printed out to the terminal.

---
Syntax to know:

* `print()` will 'print' a value. Note that this does not mean using an actual printer, but rather printing to the screen the text inside the brackets. 
* `input()` will display contents of the text inside the brackets to the user, similar to print, but will pause the program, and return the value to user entered.
  * When a command returns a value, this means you can set something equal to the command. For example, `x=max(3,4)` would set `x` equal to the return value of `max(3,4)`, which is `4`, and you would be able to use x in place of a number.
* `+` will add two variables or objects. In addition to working for addition, like `5 + 6`, it also works for adding strings, *aka text*, together, by returning a string that contains the left side followed immediately by the contents on the right side. In addition to being able to add two variable like `a = b+c`, you can also add a variable and a plain string of text, like `a = "Hello, " + c`. One common error is that you can only add a string to a string, or a number to a number. `a = 5 + c` will throw an error if `c` contains text. To avoid this, convert your numbers to strings using `str(5)`, which returns `"5"` (as a string, not a number). Finally, you may also chain addition operators like `a = b + c + d + e`.