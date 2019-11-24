# Practice problem 9

For this task, you should integrate your code from previous problems into a fully functioning bot. 

---
Basic Syntax to know:

`f = open(`filename`,`mode`)` returns a file object as f. The file must be in the same folder as the python script, and it must include the file extension. Mode is to either read from or write from the file, with `r` and `w` modes respectively.

`for line in f:` For loop that iterates over every line in the file. File has to be opened in `r` mode. Could be useful to read a file and extract key value pairs and place them into a dictionary for credential/API Key storage.

`f.write(`data`)` Writes the provided string or variable to a file, and sets itself up so that the next occurence of `write` will add after the text just inserted. `.write()` does not automatically insert a new line, so you will have to write a string containing \n, `"\n"` every time you want to go to the next line.

`f.close()` closes the file. This should be done as soon as you are done reading from the file, and before you reopen the file in a different mode.

