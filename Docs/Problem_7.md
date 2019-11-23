# Practice problem 7

For this task, you should try and create a function to dump the data from the userdictionary in the last step, into a file. You should also create a function to parse the data in the file. Furthermore, you should also create a configuration file in a format of your choosing. Your configuration file will need to store what will be the API Token for your discord bot.

Discord uses an API, Application programming interface. This is a method of communicating with discord, without using the discord program of web interface itself. The way discord, and many other services allow this is through what is specifacly known as a REST API. Instead of visiting a standard webpage, when using a RESP api, you go to a special path, discord's is `https://discordapp.com/api`, and you either request (GET), or send (POST) data to the api address. Since this is all done without any graphics, there is no place to log on, so discord allows you to obtain an API token. This is effectively your bots username and password, in one long string of characters. By providing this to discord when you use the API, you are verified and granted permission to read and send messages. 

This means that if someone has your API key, they could write there own code to read messages and reply from your bots account. On other services, your API token can be linked to your account itself, not just your bot's account, making it even worse.

To avoid putting this API Key in your code, you make a file containing the API Key in some format of your own designing, and then read that file everytime your program starts up. This way you are free to share the programs source code, knowing your API Key is safe on your computer, and not in the hands of others.

---
Syntax to know:

`f = open(`filename`,`mode`)` returns a file object as f. The file must be in the same folder as the python script, and it must include the file extension. Mode is to either read from or write from the file, with `r` and `w` modes respectively.


`f.close()` closes the file. This should be done as soon as you are done reading from the file, and before you reopen the file in a different mode.

