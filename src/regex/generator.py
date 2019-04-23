from lexer import tokens
from parser import parse


class Automata:
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def concatenate(self, other):
        nodes = []
        edges = []
        if len(self.nodes) == 0:
            return other
        elif len(other.nodes) == 0:
            return self
        else:
            size = len(self.nodes) - 1
            for node in self.nodes:
                nodes.append(node)
            for node in other.nodes[1:]:
                nodes.append(str(size + int(node)))
            for (origin, destiny, state) in self.edges:
                edges.append([origin, destiny, state])
            for (origin, destiny, state) in other.edges:
                edges.append([str(size + int(origin)), str(size + int(destiny)), state])
            return Automata(nodes, edges)

    def get_dict(self):
        return {"nodes": self.nodes, "edges": self.edges}


class CharacterAutomata(Automata):
    def __init__(self, token):
        attribute = token[1][1:-1]
        self.nodes = ["0", "1"]
        self.edges = [["0", "1", attribute[1:-1]]]


class LiteralAutomata(Automata):
    def __init__(self, token):
        attribute = token[1][1:-1]
        self.nodes = []
        self.edges = []
        for i in range(0, len(attribute)):
            self.nodes.append(str(i))
            self.edges.append([str(i), str(i + 1), attribute[i]])
        self.nodes.append(str(len(attribute)))


def generate(regex):
    ast = parse(tokens(regex))
    if len(ast) == 0:
        raise ValueError("Nothing to parse")
    node = ast[0]
    if node[0] == "CHARACTER":
        return CharacterAutomata(node)
    elif node[0] == "LITERAL":
        return LiteralAutomata(node)


print(generate('"ab"').concatenate(generate('"cd"')).get_dict())
