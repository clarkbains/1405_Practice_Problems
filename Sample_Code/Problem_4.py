def removehtml(string):
    string=string.split("<")

    for object in range(len(string)):
        if ">" in string[object]:
            string[object]=string[object].split(">")[1]

    words=""
    for object in range(len(string)):
        if string[object]!='':
            words+=str(string[object])

    print(words)

removehtml("<html><head><title>Page Title<title><head><html>")
removehtml("<a href=”p1”>Link 1</a><a href=”p2”>Link 2</a>")
removehtml("<p>Click <a href=”here.html”>here</a></p>")