def parse(tokens, ast):
    try:
        token = next(tokens)
        (name, attribute) = token
        if name == "literal":
            return (name, attribute)
    except:
        return ast


def parse_range(tokens):
    first = next(tokens)
    if first[0] != "literal":
        raise ValueError("Expected literal got: " + first[1])
    second = next(tokens)
    if second[0] != "to":
        raise ValueError("Expected to got: " + second[1])
    third = next(tokens)
    if third[0] != "literal":
        raise ValueError("Expected literal got: " + third[1])
    return [first, second, third]
