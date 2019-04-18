class ParseError(Exception):
    def __init__(self, expected, received):
        template = "Expected {0} and received ({1}, {2})"
        self.strerror = template.format(expected, received[0], received[1])
        self.args = [self.strerror]


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.next()

    def next(self):
        try:
            self.token = next(self.tokens)
        except StopIteration:
            self.token = ("EOF", "")

    def is_eof(self):
        return self.token[0] == "EOF"

    def is_character(self):
        return self.token[0] == "CHARACTER"

    def is_literal(self):
        return self.token[0] == "LITERAL"

    def is_string(self):
        return self.is_character() or self.is_literal()

    def is_comma(self):
        return self.token[0] == "COMMA"

    def is_to(self):
        return self.token[0] == "TO"

    def is_open_bracket(self):
        return self.token[0] == "OPEN_BRACKET"

    def is_close_bracket(self):
        return self.token[0] == "CLOSE_BRACKET"

    def is_open_parenthesis(self):
        return self.token[0] == "OPEN_PARENTHESIS"

    def is_close_parenthesis(self):
        return self.token[0] == "CLOSE_PARENTHESIS"

    def is_or(self):
        return self.token[0] == "OR"

    def is_not(self):
        return self.token[0] == "NOT"

    def is_plus(self):
        return self.token[0] == "PLUS"

    def is_star(self):
        return self.token[0] == "STAR"

    def is_optional(self):
        return self.token[0] == "OPTIONAL"

    def parse_alphabet_member(self):
        character = self.token
        self.next()
        if self.is_to():
            self.next()
            if self.is_character():
                lower = character
                upper = self.token
                self.next()
                return [("RANGE", [lower, upper])]
            else:
                raise ParseError("CHARACTER", self.token)
        else:
            return [character]

    def parse_alphabet(self):
        if self.is_close_bracket():
            self.next()
            return []
        elif self.is_character():
            member = self.parse_alphabet_member()
            if self.is_comma():
                self.next()
            return member + self.parse_alphabet()
        raise ParseError("CLOSE_BRACKET or CHARACTER", self.token)

    def parse_modifier(self):
        if self.is_plus():
            pass

    def parse_atom(self):
        if self.is_string():
            string = self.token
            self.next()
            return [string]
        elif self.is_not():
            self.next()
            if self.is_open_bracket():
                self.next()
                return [("NOT", ("ALPHABET", self.parse_alphabet()))]
            else:
                raise ParseError("OPEN_BRACE", self.token)
        elif self.is_open_bracket():
            self.next()
            return [("ALPHABET", self.parse_alphabet())]
        elif self.is_open_parenthesis():
            self.next()
            group = self.parse_group()
            if self.is_plus():
                self.next()
                return [("PLUS", ("GROUP", group))]
            elif self.is_star():
                self.next()
                return [("STAR", ("GROUP", group))]
            elif self.is_optional():
                self.next()
                return [("OPTIONAL", ("GROUP", group))]
            else:
                return [("GROUP", group)]
        raise ParseError("STRING or OPEN_BRACKET or OPEN_PARENTHESIS", self.token)

    def parse_or(self):
        atom = self.parse_atom()
        if self.is_or():
            self.next()
            return atom + self.parse_or()
        else:
            return atom

    def parse_expression(self):
        atom = self.parse_atom()
        if self.is_or():
            self.next()
            return [("OR", atom + self.parse_or())]
        else:
            return atom

    def parse_group(self):
        if self.is_close_parenthesis():
            self.next()
            return []
        else:
            return self.parse_expression() + self.parse_group()

    def parse(self):
        if self.is_eof():
            return []
        else:
            return self.parse_expression() + self.parse()


def parse(tokens):
    parser = Parser(tokens)
    return parser.parse()


ast = parse(
    iter(
        [
            ("LITERAL", "hello"),
            ("OPEN_PARENTHESIS", "("),
            ("LITERAL", "ONE"),
            ("OR", "|"),
            ("LITERAL", "TWO"),
            ("OR", "|"),
            ("LITERAL", "THREE"),
            ("OPEN_PARENTHESIS", "("),
            ("LITERAL", "ONE"),
            ("LITERAL", "TWO"),
            ("LITERAL", "THREE"),
            ("CLOSE_PARENTHESIS", ")"),
            ("OPTIONAL", "?"),
            ("CLOSE_PARENTHESIS", ")"),
            ("NOT", "~"),
            ("OPEN_BRACKET", "["),
            ("CHARACTER", "a"),
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
    )
)

print(ast)
