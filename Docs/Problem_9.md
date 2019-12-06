# Practice problem 9

For this task, you should try and create a function to dump the data from the userdictionary in the last step, into a file. You should also create a function to parse the data in the file. Furthermore, you should also create a configuration file in a format of your choosing. Your configuration file will need to store what will be the API Token for your discord bot.

Discord uses an API, Application programming interface. This is a method of communicating with discord, without using the discord program of web interface itself. The way discord, and many other services allow this is through what is specifacly known as a REST API. Instead of visiting a standard webpage, when using a REST api, you go to a special path, discord's is `https://discordapp.com/api`, and you either request (GET), or send (POST) data to the api address. Since this is all done without any graphics, there is no place to log on, so discord allows you to obtain an API token. This is effectively your bots username and password, in one long string of characters. By providing this to discord when you use the API, you are verified and granted permission to read and send messages. 

This means that if someone has your API key, they could write there own code to read messages and reply from your bots account. On other services, your API token can be linked to your account itself, not just your bot's account, making it even worse.

To avoid putting this API Key in your code, you make a file containing the API Key in some format of your own designing, and then read that file everytime your program starts up. This way you are free to share the programs source code, knowing your API Key is safe on your computer, and not in the hands of others. It may be useful to create another script which prompts the user for theior key, and writes it in a format readable by the main script.

You may install the JSON module, which will turn a dictionary, list or variable into a human readable format, amd is able to do the reverse. This way you can write a variable and read a variable to a file. It should already be installed on your system.

Make your program store the main info, so if doesn't loose info when restarted.

---
Basic Syntax to know:
`import('json')` will import the json library, allowing you to write and read variables to files.

`f = open(`filename`,`mode`)` returns a file object as f. The file must be in the same folder as the python script, and it must include the file extension. Mode is to either read from or write from the file, with `r` and `w` modes respectively.

`for line in f:` For loop that iterates over every line in the file. File has to be opened in `r` mode. Could be useful to read a file and extract key value pairs and place them into a dictionary for credential/API Key storage.

`f.write(`data`)` Writes the provided string or variable to a file, and sets itself up so that the next occurence of `write` will add after the text just inserted. `.write()` does not automatically insert a new line, so you will have to write a string containing \n, `"\n"` every time you want to go to the next line.

`json.load(f)` converts a JSON file to the python equivalent variable. Reads from the file f, opened with the open command above.
`json.dump(` var `, f)` writes the variable in JSON to the file f, opened with the open command above. Make sure to open the file in `w` mode.

`f.close()` closes the file. This should be done as soon as you are done reading from the file, and before you reopen the file in a different mode.

[reference 1](https://www.w3schools.com/python/python_file_handling.asp)

[reference 2](https://www.w3schools.com/python/python_file_open.asp)