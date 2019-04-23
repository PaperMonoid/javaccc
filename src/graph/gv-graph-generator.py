import os
import platform


class GVGraphGenerator:
    def __init__(self, nodes=[], edges=[], graph_name='automata', path = os.getcwd()):
        self.graph_name = graph_name  # files name
        self.extension = '.gv'  # extension
        self.path = path # path to save .gv and .png file
        self.nodes = nodes  # list within states [0,1,2,...,n]
        # list within edges [[origin, destiny, symbol],[origin, destiny, symbol],...,n]
        self.edges = edges
        self.doc = '' # contains the document

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
            self.doc = self.doc + row
            # next node
            c = c + 1

        # make initial point and arrow to the first node
        row = '\n\tnode [shape = point ]; qi\n\tqi -> n0;\n'.format()
        self.doc = self.doc + row

        return

    def GenerateEdges(self):
        row = ''.format()
        # for each edge
        for edge in self.edges:
            # make arrow/union with its label
            row = '\n\tn{0} -> n{1} [ label = \"{2}\" ];'.format(
                edge[0], edge[1], edge[2])
            self.doc = self.doc + row
        
        return

    def BuildDocument(self):
        row = ''.format()

        # add first line
        row = 'digraph finite_state_machine {{'.format()
        self.doc = self.doc + row

        # orientation for the image
        row = '\n\trankdir=LR;'.format()
        self.doc = self.doc + row

        # size , I'm noy sure size of what ? xd
        row = '\n\tsize="8,5"'.format()
        self.doc = self.doc + row

        # call GenerateNodes
        self.GenerateNodes()
        # call GenerateEdges
        self.GenerateEdges()

        # last line of the file
        row = '\n}}'.format()
        self.doc = self.doc + row

        return        

    def Save(self,path = os.getcwd()):
        # determinate path
        if self.path == '':
            self.path = path
        elif path == '':
            self.path = self.path

        try:
            # create the file
            f = open(self.path + '/' + self.graph_name + self.extension, 'w', encoding='utf-8')
            f.write(self.doc)
            # close file
            f.close()

            # if OS is linux or windows, build image
            so = platform.system().lower()
            if so == 'linux' or so == 'windows':
                # command for build imagen [graphviz is required]
                os.system('dot -Tpng {0}/{1}.gv -o {0}/{1}.png'.format(self.path,self.graph_name))
        except Exception as e:
            print('Something went wrong -> \n {0}'.format(e))

        return