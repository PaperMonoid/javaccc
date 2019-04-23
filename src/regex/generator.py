def charset_create(lower=32, upper=126):
    charset = []
    for char in range(lower, upper):
        charset.append(chr(char))
    return charset


def charset_union(first, second):
    charset = []
    for char in first:
        charset.append(char)
    for char in second:
        if char not in charset:
            charset.append(char)
    return charset


def charset_difference(first, second):
    charset = []
    for char in first:
        if char not in second:
            charset.append(char)
    return charset


ascii_charset = charset_create()


def charset_complement(first):
    return charset_difference(ascii_charset, first)


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

    @staticmethod
    def parse(ast):
        automatas = []
        for child in ast:
            if child[0] == "CHARACTER":
                automatas.append(CharacterAutomata(child))
            elif child[0] == "LITERAL":
                automatas.append(LiteralAutomata(child))
            elif child[0] == "ALPHABET" or child[0] == "NOT":
                automatas.append(CharacterClassAutomata(child))
        return Automata.union(automatas)

    @staticmethod
    def union(others):
        nodes = ["0"]
        edges = []
        if len(others) == 0:
            return Automata()
        if len(others) == 1:
            return others[0]
        last = 1
        for other in others:
            last = last + len(other.nodes)
        i = 1
        for other in others:
            for node in other.nodes:
                nodes.append(str(i + int(node)))
            edges.append(["0", str(i), ""])
            for (origin, destiny, state) in other.edges:
                edges.append([str(i + int(origin)), str(i + int(destiny)), state])
            i = i + len(other.nodes)
            edges.append([str(i - 1), str(last), ""])
        nodes.append(str(last))
        return Automata(nodes, edges)

    def get_dict(self):
        return {"nodes": self.nodes, "edges": self.edges}


class CharacterAutomata(Automata):
    def __init__(self, token):
        attribute = token[1][1:-1]
        self.nodes = ["0", "1"]
        self.edges = [["0", "1", attribute]]


class LiteralAutomata(Automata):
    def __init__(self, token):
        attribute = token[1][1:-1]
        self.nodes = []
        self.edges = []
        for i in range(0, len(attribute)):
            self.nodes.append(str(i))
            self.edges.append([str(i), str(i + 1), attribute[i]])
        self.nodes.append(str(len(attribute)))


class CharacterClassAutomata(Automata):
    def __init__(self, ast):
        not_flag = False
        if ast[0] == "NOT":
            ast = ast[1]
            not_flag = True
        charset = []
        for token in ast[1]:
            if token[0] == "CHARACTER":
                attribute = token[1][1:-1]
                charset = charset_union(charset, [attribute])
            elif token[0] == "RANGE":
                [lower_character, upper_character] = token[1]
                lower = ord(lower_character[1][1:-1])
                upper = ord(upper_character[1][1:-1])
                charset = charset_union(charset, charset_create(lower, upper))
        if not_flag:
            charset = charset_complement(charset)
        automatas = []
        for char in charset:
            token = ("CHARACTER", '"{0}"'.format(char))
            automatas.append(CharacterAutomata(token))
        automata = Automata.union(automatas)
        self.nodes = automata.nodes
        self.edges = automata.edges
