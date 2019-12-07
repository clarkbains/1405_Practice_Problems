# Practice problem 4
This problem tracks as you edit the menu from the last practice problem to allow exiting from the loop.


---
Syntax to know:

* `break` will exit from a loop, skipping any code at the end and continuing after the loop. See the example below

```python
counter = 0
while True:
        print ("Counter is now at" + str(counter))
        if counter == 2:
            print ("Breaking")       
        counter = counter + 1
print ("Counter finished at " + str(counter))
```
will output the following:
```
Counter is now at 0
Counter is now at 1
Counter is now at 2
Breaking
Counter finished at 2

```
