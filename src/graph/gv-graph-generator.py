import datetime


class GVGraphGenerator:
    def __init__(self, graph_name='automata', nodes=[], edges=[]):
        self.graph_name = graph_name
        self.extension = '.gv'
        self.nodes = nodes  # list within states [0,1,2,...,n]
        # list within edges [[origin, destiny, symbol],[origin, destiny, symbol],...,n]
        self.edges = edges

        self.f = open(self.graph_name + self.extension, 'w', encoding='utf-8')
        self.f.close()

        # automata's nodes and edges [for test only]
        self.nodes = list(['0', '1', '2', '3'])  # states
        self.edges = list([['0', '1', 'a'], ['0', '2', 'b'], ['1', '1', 'b'], ['1', '2', 'c'], [
                          '2', '2', 'b'], ['2', '3', 'b'], ['2', '1', 'g']])  # [origin, destiny, symbol]

        # here we go
        self.BuildDocument()

    def GenerateNodes(self):
        row = ''.format()
        # build graph
        c = 0
        while c < len(self.nodes):
            if c == 0 or c == (len(self.nodes) - 1):
                row = '\n\n\tnode [ shape = doublecircle, label = "{0}", fontsize  = 14] n{0};\n'.format(
                    self.nodes[c])
            else:
                row = '\n\tnode [ shape = circle, label = "{0}", fontsize  = 12] n{0};'.format(
                    self.nodes[c])
            self.f.write(row)
            c = c + 1

        row = '\n\tnode [shape = point ]; qi\n\tqi -> n0;\n'.format()
        self.f.write(row)

        return

    def GenerateEdges(self):
        row = ''.format()
        for node in self.edges:
            row = '\n\tn{0} -> n{1} [ label = \"{2}\" ];'.format(
                node[0], node[1], node[2])
            self.f.write(row)
        return

    def BuildDocument(self):
        self.f = open(self.graph_name + self.extension, 'w', encoding='utf-8')
        row = ''.format()

        row = 'digraph finite_state_machine {{'.format()
        self.f.write(row)

        row = '\n\trankdir=LR;'.format()
        self.f.write(row)

        row = '\n\tsize="8,5"'.format()
        self.f.write(row)

        # call GenerateNodes
        self.GenerateNodes()
        # call GenerateEdges
        self.GenerateEdges()

        row = '\n}}'.format()
        self.f.write(row)

        self.f.close()

        return


gg = GVGraphGenerator('test', [], [])
