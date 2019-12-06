# Practice problem 6
 
--- 

This problem will take a little bit of a break from the bot code to introduce for loops and lists

The goal of this task will be to create a list or dictionary containing items, and print contents on command. This should be done using for and while loops as much as possible. Looping, lists, and dictionaries will be heavily used in the final bot.

---
Syntax to know:

1. `[]` is how an empty list is declared in python. A list is a collection of variables, that can all be accessed easily programmatically. For example, in previous problems, if you needed to hold 4 pieces of data, you would use 4 variables, `var1`,`var2`,`var3` and `var4`. Using a list, you can declare `var = ["Value1", "Value2", "Value3", "Value4"]` , and access the values using `var[0]` up to `var[3]`. These would be `"Value1"` and `"Value4"` respectively, just how if Note that the value in square brackets is the index, which is typically a positive integer. The index starts at 0, and goes up to the length of the list minus 1. Negative indexes start from the end of the list, is such a way that `var[-1]` would be the last element. See the IDLE shell below for a programmatic explanation.
   * List Functions:
     
     * list.`pop(x=len(`list`))` Removes and returns the first item of the array if no `x` value is specified, otherwise removes and returns element at `x`
     * list.`append(x)` Adds `x` to the end of the array
     * string.`split(val = " ")` returns a list. Passing an argument sets the value to split on, which defaults to a space. Every occurrence of the value to split on is removed, and text in between will be added as a new list element.
     * `len(`list`)` Returns the length of the array. 
2. `{}` is how an empty dictionary is declared in python. A dictionary is just like a list, but instead of using numbers as the index, the index can be text. The index is instead called a key, and the associated value is simply called the value.
3. `for `var `in` list/dictionary`:` Similar to an `while` block in terms of syntax. Will loop through the contained code, setting var to the next element or key in the list/dictionary after each loop. Useful to perform an operation on every element, like printing
4. `range(start,end,step)` returns a list like object of integers, starting at `start` and incrementing by `step` up to but not including `end`.  Omitting `start` and `step` and only passing `end` is equivalent to a `start` of 0 and `step` of 1. Useful in conjunction with `len(`list`)` to loop through the indexes of a list, or with a single integer argument to loop through the same code `end` times.

Lists
```python
Python 3.7.5rc1 (default, Oct  8 2019, 16:47:45) 
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> list1 = []
>>> print (list1)
[]
>>> list1.append("Adds to the end of the list")
>>> print (list1)
['Adds to the end of the list']
>>> list1.append("New ending element")
>>> print (list1)
['Adds to the end of the list', 'New ending element']
>>> list1.append(6)
>>> print (list1)
['Adds to the end of the list', 'New ending element', 6]
>>> len (list1)
3
>>> idex1 = 1
1
>>> list1[0]
'Adds to the end of the list'
>>> list1[1]
'New ending element'
>>> list1[idex1]
'New ending element'
>>> list1[2]
6
>>> list1[-1]
6
>>> list1[-2]
'New ending element'
>>> len(list1)
3
>>> list1[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> list1.pop()
6
>>> print (list1)
['Adds to the end of the list', 'New ending element']
>>> list1.pop(0)
'Adds to the end of the list'
>>> print (list1)
['New ending element']
>>> list2 = ["Elm0", "Elm1", "Elm2"]
>>> list2[1]
'Elm1'
>>> list2[1] = "New Value"
'Elm1'
>>> print (list2)
['Elm0', 'New Value', 'Elm2']
>>> "Hi,My name,is,Clark".split(',')
['Hi', 'My name', 'is', 'Clark']

```
Dictionarys 
```python
>>> a = {}
>>> a["b"] = "val"
>>> a["c"] = "val2"
>>> a["a"] = "val0"
>>> print(a)
{'b': 'val', 'c': 'val2', 'a': 'val0'}
>>> a["b"]
'val'
>>> a["b"] = "Not Val"
>>> a["b"]
'Not Val'
>>> print(a)
{'b': 'Not Val', 'c': 'val2', 'a': 'val0'}
>>> a = {'key' : 'val', 'key2' : 'vale'}
{'key' : 'val', 'key2' : 'vale'}
```

[List Reference](http://python-ds.com/python-3-list-methods)

[Dictionary Official Reference](https://docs.python.org/3/tutorial/datastructures.html) - Will be a bit harder to understand, but this is more or less what all official language documentation will look like.

[Simpler Dictionary Reference](https://www.tutorialspoint.com/python3/python_dictionary.htm)