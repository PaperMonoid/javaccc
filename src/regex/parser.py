def parse(tokens, ast=[]):
    try:
        (token, attribute) = next(tokens)
    except:
        pass
