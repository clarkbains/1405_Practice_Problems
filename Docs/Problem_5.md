# Practice problem
 

This problem will introduct functions

Functions are an easy way to clarify code, and repeat code in multiple places without really repeating the entire code. A function is a block of self contained code, given a name, input values, and an output value. By writing a function, like `promptForInput(msg, type)`, you would be able to simply call `response = promptForInput("Enter a number", "num")` and then your code contained inside the function would run, potentially repeating the message until if got a value that matches a set of rules for a `num`, like potentially being a positive digit. This way, the 5 or so lines it takes to do this don't need to be repeated throughout your code, and are in one central spot if they need modification, updating or otherwise. 

---
Syntax to know:

1. `def` functionname `(`arg1`,`arg2`):` is how you define a function. Functions should generally be declared at the top of your code for python, unless you know what you are doing. You may have as many arguments as needed. The name of the arguments can be completely arbitrary. For example, if the function was defined as below, you can call `multiplybynumber(a,b)`, where `a` and `b` can be variables or values by themselves. Note that you can read from, but not write to variable declared outside the function, from inside the function by default. The exception to this is using list and dictionary methods, like `append(`val`)`, `pop()`. To be able to write to all variable types from inside a function, add `global variable_name` as the first line of the function. Multiple variables can be added, separated by commas. 
   ```python 
   def multiplybynumber (num1,num2):
     print (num1*num2)
      ```
2. `return` can only be called from inside a function. This will return a value to the function itself, in such a way that if the `print` were swapped for `return` in the above example and the brackets removed, running `result = multiplybynumber(5,6)` would result in `result` having a value of `20`