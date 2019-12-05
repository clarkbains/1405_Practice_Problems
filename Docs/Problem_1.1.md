# Practice problem 1
This task tracks as you extend the basic greeter to repeatedly loop ask for a users name, and in addition to greeting the current person, you should say goodbye to the last person once the new person enters some text
```
>What is your name? Clark

Hi Clark
>What is your name? Bob
Bye Clark
Hi Bob
>What is your name?
^C
```
Note that `^C` simply means that `ctrl`+`c` was pressed in the terminal. This kills the program and exits out of the infinite loop.

---
Syntax to know:

* `print()` will 'print' a value. Note that this does not mean using an actual printer, but rather printing to the screen the text and variables inside the brackets. 
* `while ` condition `:` will repeat the code contained within it while the condition is true. (Example at bottom)
  
* Comparison Operators (Samples at bottom)
  * a`==`b Checks if left side is the same as the right side. Evaluates to true if they do.
  * a `in` b Checks if a contains text in b, or is equal
  * a `>` b Evaluates true if a is greater than b
  * a `>=` b Evaluates true if a is greater than or equal to b
  * a `<=` b Evaluates true if a is less than b
  * a `<` b Evaluates true if a is less than b
* Not quite comparison operators, but still useful for conditions
  * `True` this will always be true, and is good for infinite loops when used with while
  * `False` this will always be false
  * condition1 `or` condition2 will evaluate true if one or the other condition is true
  * condition1 `and` condition2 will evaluate true is both conditions are true
  * `not` condition1 will flip the result of condition 1. If condition 1 is true, then `not` condition 1 will be false.

Example While Loop
```python
while true:
    name = input ("Hello, What is your name? ")
    outMsg = "Hello, " + name + ". It is good to meet you. How can I help you today?"
    print (outMsg)
```
Sample Comparison Operators
```python
Python 3.7.5 (default, Nov 20 2019, 09:21:52) 
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = "abc"
>>> b = True
>>> c = 49
>>> d = 89
>>> e = 89
>>> d==e
True
>>> d==c
False
>>> d>c
True
>>> d>=c
True
>>> d>489
False
>>> a == "abc"
True
>>> not a == "abc"
False
>>> a == b
False
>>> a == b or a == "abc"
True
>>> a == b and a == "abc"
False
```
