from lexer import tokens

""" read example file """
f = open("examples.txt", "r")
examples = f.read()
f.close()

""" prints tokens """
for (token, attribute) in tokens(examples):
    print("{0}: {1}".format(token, attribute))
