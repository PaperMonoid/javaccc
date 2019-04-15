import re

""" regular expressions to match """
regexs = [
    ("LITERAL", '"((\\\.)|[^"])*"'),
    ("CHARACTER", '"((\\\.)|[^"])?"'),
    ("OPEN_PARENTHESIS", "\("),
    ("CLOSE_PARENTHESIS", "\)"),
    ("OPEN_BRACKET", "\["),
    ("CLOSE_BRACKET", "\]"),
    ("OR", "\|"),
    ("NOT", "~"),
    ("PLUS", "\+"),
    ("STAR", "\*"),
    ("OPTIONAL", "\?"),
    ("COMMA", ","),
    ("TO", "-"),
]


def next_token(blob):
    """ gets the closest largest token """
    key = None
    match = None
    for (new_key, value) in regexs:
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
