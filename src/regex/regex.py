from regex.lexer import tokens
from regex.parser import parse
from regex.generator import generate
from regex.optimizer import optimize


def Regex(regex, optimize_flag=False):
    ast = parse(tokens(regex))
    if len(ast) == 0:
        raise ValueError("Nothing to parse")
    automata = generate(ast)
    if optimize_flag:
        return optimize(automata)
    else:
        return automata
