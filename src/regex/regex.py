from regex.lexer import tokens
from regex.parser import parse
from regex.generator import generate
from regex.optimizer import optimize


def Regex(regex):
    ast = parse(tokens(regex))
    if len(ast) == 0:
        raise ValueError("Nothing to parse")
    automata = generate(ast)
    return optimize(automata)
