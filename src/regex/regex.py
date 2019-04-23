from regex.lexer import tokens
from regex.parser import parse
from regex.generator import *


def Regex(regex):
    ast = parse(tokens(regex))
    if len(ast) == 0:
        raise ValueError("Nothing to parse")
    node = ast[0]
    if node[0] == "CHARACTER":
        return CharacterAutomata(node)
    elif node[0] == "LITERAL":
        return LiteralAutomata(node)
    elif node[0] == "ALPHABET" or node[0] == "NOT":
        return CharacterClassAutomata(node)
