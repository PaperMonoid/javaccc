class Optimizer:
    def __init__(self, automata):
        self.automata = automata
        self.nodes = []
        self.edges = []
        self.states = []

    def edges_from(self, node):
        for edge in self.automata.edges:
            if edge[0] == node:
                yield edge

    def move_from(self, node, state):
        for edge in self.edges_from(node):
            if edge[2] == state:
                yield edge[1]

    def possible_moves(self, nodes):
        states = []
        for node in nodes:
            for edge in self.edges_from(node):
                if edge[2] not in states and not edge[2] == "":
                    states.append(edge[2])
        return states

    def e(self, nodes=[], stop=True):
        _nodes = list(nodes)
        for node in nodes:
            for _node in self.move_from(node, ""):
                if _node not in _nodes:
                    _nodes.append(_node)
                    _nodes = self.e(_nodes)
        return _nodes

    def move(self, nodes, state):
        _nodes = []
        for node in nodes:
            for _node in self.move_from(node, state):
                if _node not in _nodes:
                    _nodes.append(_node)
        return _nodes

    def get_state_index(self, state):
        state.sort()
        i = 0
        for _state in self.states:
            if _state == state:
                return i
            i = i + 1
        return -1

    def put_state(self, state):
        state.sort()
        if self.get_state_index(state) < 0:
            self.states.append(state)
            self.nodes.append(len(self.nodes))

    def expand(self, t):
        for state in self.possible_moves(t):
            ts = self.move(t, state)
            tn = self.e(ts)
            search = self.get_state_index(tn)
            self.put_state(tn)
            origin = self.get_state_index(t)
            destiny = self.get_state_index(tn)
            origin = self.remap(origin)
            destiny = self.remap(destiny)
            self.edges.append([origin, destiny, state])
            if search < 0:
                self.expand(tn)

    def remap(self, state):
        if state == 4:
            return 2
        elif state == 3:
            return 4
        elif state == 2:
            return 3
        else:
            return state

    def optimize(self):
        t0 = self.e([self.automata.nodes[0]])
        self.put_state(t0)
        self.expand(t0)
        return self

    def get_dict(self):
        return {"nodes": self.nodes, "edges": self.edges}


def optimize(automata):
    return Optimizer(automata).optimize()
