import re

# read example file
f = open("examples.txt", "r")
examples = f.read();
f.close()

# regular expressions to match
regexs = {
    "literal": "\"((\\\.)|[^\"])*\"",
    "open_parenthesis": "\(",
    "close_porenthesis": "\)",
    "open_bracket": "\[",
    "close_bracket": "\]",
    "or": "\|",
    "not": "~",
    "plus": "\+",
    "star": "\*",
    "optional": "\?",
    "comma": ",",
    "to": "-"
}

# gets the closest and largest token
def next_token(blob):
    key = None
    match = None
    for new_key, value in regexs.items():
        new_match = re.search(value, blob)
        if match is None:
            key = new_key
            match = new_match
        elif new_match is not None:
            if new_match.start() < match.start():
                key = new_key
                match = new_match
            elif (new_match.start() == match.start() and
                  new_match.end() >= match.end()):
                key = new_key
                match = new_match
    if key is None or match is None:
        return None
    else:
        return (key, match)

blob = examples
tokens = []
token = next_token(blob)

# matches tokens in blob
while token is not None:
    tokens.append(token)
    blob = blob[token[1].end(0):]
    token = next_token(blob)

# prints tokens
for token in tokens:
    print("{0}: {1}".format(token[0], token[1].group(0)))
