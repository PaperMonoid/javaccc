from regex.lexer import tokens
from regex.parser import parse
from regex.generator import Automata


def Regex(regex):
    ast = parse(tokens(regex))
    if len(ast) == 0:
        raise ValueError("Nothing to parse")
    return Automata.parse(ast)
