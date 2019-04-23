import os
from sys import platform


class GVGraphGenerator:
    def __init__(self, graph_name='automata', nodes=[], edges=[]):
        self.graph_name = graph_name  # files name
        self.extension = '.gv'  # extension
        self.nodes = nodes  # list within states [0,1,2,...,n]
        # list within edges [[origin, destiny, symbol],[origin, destiny, symbol],...,n]
        self.edges = edges

        # create the file, only for be sure
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
        # while c < nodes lenght
        while c < len(self.nodes):
            # if node is the first or the last
            if c == 0 or c == (len(self.nodes) - 1):
                # make it, within doublecircle
                row = '\n\n\tnode [ shape = doublecircle, label = "{0}", fontsize  = 14] n{0};\n'.format(
                    self.nodes[c])
            else:
                # else, make it, withit simple circle
                row = '\n\tnode [ shape = circle, label = "{0}", fontsize  = 12] n{0};'.format(
                    self.nodes[c])
            self.f.write(row)
            # next node
            c = c + 1

        # make initial point and arrow to the first node
        row = '\n\tnode [shape = point ]; qi\n\tqi -> n0;\n'.format()
        self.f.write(row)

        return

    def GenerateEdges(self):
        row = ''.format()
        # for each edge
        for edge in self.edges:
            # make arrow/union with its label
            row = '\n\tn{0} -> n{1} [ label = \"{2}\" ];'.format(
                edge[0], edge[1], edge[2])
            self.f.write(row)
        return

    def BuildDocument(self):
        # open the file again, in write mode
        self.f = open(self.graph_name + self.extension, 'w', encoding='utf-8')
        row = ''.format()

        # add first line
        row = 'digraph finite_state_machine {{'.format()
        self.f.write(row)

        # orientation for the image
        row = '\n\trankdir=LR;'.format()
        self.f.write(row)

        # size , I'm noy sure size of what ? xd
        row = '\n\tsize="8,5"'.format()
        self.f.write(row)

        # call GenerateNodes
        self.GenerateNodes()
        # call GenerateEdges
        self.GenerateEdges()

        # last line of the file
        row = '\n}}'.format()
        self.f.write(row)

        # close file
        self.f.close()

        # if OS is linux or linux2, build image
        if platform == "linux" or platform == "linux2":
            self.BuildImage()

        return

    def BuildImage(self):
        try:
            # command for build imagen [graphviz is required]
            os.system("dot -Tpng {0}.gv -o {0}.png".format(self.graph_name))
        except Exception as e:
            print('Something went wrong -> \n {0}'.format(e))
        return


gg = GVGraphGenerator('test', [], [])
