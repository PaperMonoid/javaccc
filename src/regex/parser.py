def parse(tokens, ast):
    try:
        (name, attribute) = next(tokens)
        if name == "open_parenthesis":
            pass
        elif name == "close_parenthesis":
            pass
        else:
            return parse(tokens, ast)
    except:
        return ast
