import re

""" regular expressions to match """
regexs = {
    "literal": '"((\\\.)|[^"])*"',
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
    "to": "-",
}


def next_token(blob):
    """ gets the closest largest token """
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
            elif new_match.start() == match.start() and new_match.end() >= match.end():
                key = new_key
                match = new_match
    if key is None or match is None:
        return None
    else:
        return (key, match)


def tokens(blob):
    """ matches tokens in blob """
    token = next_token(blob)
    while token is not None:
        (key, match) = token
        blob = blob[match.end(0) :]
        token = next_token(blob)
        yield (key, match.group(0))
