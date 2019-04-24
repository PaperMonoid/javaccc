tokens = dict()

def BuildTokens():
    global tokens
    for token, regex in tokens.items():
        msj = "TOKEN:\n{{\n\t//TOKEN's name: {0}\n\t<{0}: {1}>{{  }} : DEFAULT\n}}".format(token,regex)
        print(msj)
    return

def MatchFile(path):
    global tokens
    # open the file, read row by row
    f = open(path, "r")
    for row in f:
        # for each row in the file
        # split the row in words
        words = row.split(",")
        #if the token is not created, add it
        if words[0] in tokens:
            regex = "|\"{0}\"".format(words[1][:-1])
            tokens[words[0]] = tokens[words[0]] + regex
            
        else:
            regex = "\"{0}\"".format(words[1][:-1])
            tokens[words[0]] = regex
    BuildTokens()
    return

go = True
while(go):
    # input a file path
    path = input("Input a file path [.cvs] with the tokens table [<tokens name>,<regex>]: ")
    MatchFile(path)

    # new input?
    answer = input("\nNew input file?[y/n]: ")
    if(answer == "n"):
        go = False
    else:
        go = True
