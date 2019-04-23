#GVGraphGenerator

GVGraphGenerator is a small Python script that helps us generate the necessary code to generate an .png image of an automata. The necessary information is a string with the name of the file, a list with the nodes, and a list with the unions. The script requires to have the [Graphviz](http://www.graphviz.org/) software installed. For Windows, it will only generate the .gz file. For linux, it will build the image for you.

For its use:

Declarate the list within states like \['0','1','2',...,'n'\]:
`nodes = list(['0', '1', '2', '3']) # states`

Declarate the list within edges like [[origin, destiny, symbol],[origin, destiny, symbol],...,n]:
`edges = list([['0', '1', 'a'], ['0', '2', 'b'], ['1', '1', 'b'], ['1', '2', 'c'], ['2', '2', 'b'],['2', '3', 'b'], ['2', '1', 'g']]) # [origin, destiny, symbol]`

Instance and call the constructor:
`gg = GVGraphGenerator('test',nodes,edges)`

Output:
[(https://github.com/PaperMonoid/javaccc/blob/master/src/graph/test.png)](https://github.com/PaperMonoid/javaccc/blob/master/src/graph/test.png)
