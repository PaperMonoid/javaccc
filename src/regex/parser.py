class ParseError(Exception):
    def __init__(self, expected, received):
        template = "Expected {0} and received ({1}, {2})"
        self.strerror = template.format(expected, received[0], received[1])
        self.args = [self.strerror]


def is_character(token):
    return token[0] == "CHARACTER"


def is_literal(token):
    return token[0] == "LITERAL"


def is_string(token):
    return is_character(token) or is_literal(token)


def is_comma(token):
    return token[0] == "COMMA"


def is_to(token):
    return token[0] == "TO"


def is_open_bracket(token):
    return token[0] == "OPEN_BRACKET"


def is_close_bracket(token):
    return token[0] == "CLOSE_BRACKET"


def parse(tokens, ast):
    try:
        token = next(tokens)
        if is_string(token):
            return token
        elif is_open_bracket(token):
            return parse_alphabet(tokens, [])
    except ParseError as error:
        print(error)
        return ast
    except:
        return ast


def parse_alphabet(tokens, ast):
    token = next(tokens)
    if is_close_bracket(token):
        return ast
    elif is_character(token):
        first = token
        token = next(tokens)
        if is_close_bracket(token):
            return ast + [first]
        elif is_comma(token):
            return parse_alphabet(tokens, ast + [first])
        elif is_to(token):
            token = next(tokens)
            if is_character(token):
                second = token
                token = next(tokens)
                if is_close_bracket(token):
                    return ast + [[first, second]]
                elif is_comma(token):
                    return parse_alphabet(tokens, ast + [[first, second]])
            else:
                raise ParseError("CHARACTER", token)
        else:
            raise ParseError("CLOSE_BRACKET or COMMA or TO", token)
    raise ParseError("CLOSE_BRACKET or CHARACTER", token)


ast = parse(
    iter(
        [
            ("OPEN_BRACKET", "["),
            ("STRING", "a"),
            ("COMMA", ","),
            ("CHARACTER", "e"),
            ("COMMA", ","),
            ("CHARACTER", "i"),
            ("COMMA", ","),
            ("CHARACTER", "o"),
            ("COMMA", ","),
            ("CHARACTER", "u"),
            ("TO", "-"),
            ("CHARACTER", "a"),
            ("COMMA", ","),
            ("CHARACTER", "a"),
            ("CLOSE_BRACKET", "]"),
        ]
    ),
    [],
)

print(ast)
