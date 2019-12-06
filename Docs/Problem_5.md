# Practice problem 5
This problem tracks as you edit the menu from the last practice problem to involve multiple levels, and loop repeatedly through it


At the main level, add another option to edit a mark. Within this option, you should be able to pick a course (Can be any course for now, irrespective of the add course option), then add, edit or remove a grade. A grade consists of both a mark, and a weight. (None of these have to be kept track of. Just print a message saying what has been done)

In addition, your code should match the following two criteria

1. You must use `elif` blocks where applicable
2. You must separate the inputs from the outputs. Ask for the required inputs in one `if`/`elif` set of block, and print them in another set of `if`/`elif` blocks. This will be useful for later. Use a variable to keep track of where your program will need to go to print the output. 

---
Syntax to know:

* `elif {condition}:` Must follow an `if` or `elif` block immediately after the code inside is finished. Should be indented the same as the accompanying conditional blocks. Similar to `if`, `elif` will run the indented code below it if the condition evaluates to true. In an `if`/`elif`/`else`, once the code in the first block's with a true `{condition}` is run, the chain breaks, and jumps to the line immediately after the last `elif`/`else`.
* `else:` If none of the conditions in an `if`/`elif` chain are true, then the else block executes the code contained inside (indented)
* `float()` Similar to `int()` and `string()`. This is a datatype used to hold decimal numbers. Sometimes you will see small values at the end, like `3.0000000017` due to the way this math works on base-2 (binary) computers, versus the base-10 we use in everyday math

[Conditional Reference](https://www.python-course.eu/python3_conditional_statements.php)


