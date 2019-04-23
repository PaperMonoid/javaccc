# GVGraphGenerator

GVGraphGenerator is a small Python script that helps us generate the necessary code to generate an .png image of an automata. The necessary information is a string with the name of the file, a list with the nodes, and a list with the edges. The script requires to have the [Graphviz](http://www.graphviz.org/) software installed. For Windows and Linux, it will build the image for you.

## For its use

First, import module to your project.

Declarate the list within states like \['0','1','2',...,'n'\]:

`nodes = list(['0', '1', '2', '3']) # states`

Declarate the list within edges like [[origin, destiny, symbol],[origin, destiny, symbol],...,n]:

`edges = list([['0', '1', 'a'], ['0', '2', 'b'], ['1', '1', 'b'], ['1', '2', 'c'], ['2', '2', 'b'],['2', '3', 'b'], ['2', '1', 'g']]) # [origin, destiny, symbol]`

Instance and call the constructor:

`gg = GVGraphGenerator(nodes=nodes,edges=edges,[graph_name='<graph name>'],[path='<path to save>'])`

Save your graph:

`gg.Save([path='<path to save>'])`

If a path is not provided, it is saved in the current path.

## Output

automata.gv file:

```
digraph finite_state_machine {
	rankdir=LR;
	size="8,5"

	node [ shape = doublecircle, label = "0", fontsize  = 14] n0;

	node [ shape = circle, label = "1", fontsize  = 12] n1;
	node [ shape = circle, label = "2", fontsize  = 12] n2;

	node [ shape = doublecircle, label = "3", fontsize  = 14] n3;

	node [shape = point ]; qi
	qi -> n0;

	n0 -> n1 [ label = "a" ];
	n0 -> n2 [ label = "b" ];
	n1 -> n1 [ label = "b" ];
	n1 -> n2 [ label = "c" ];
	n2 -> n2 [ label = "b" ];
	n2 -> n3 [ label = "b" ];
	n2 -> n1 [ label = "g" ];
}
```

automata.png file:

![automata.png](https://github.com/PaperMonoid/javaccc/blob/master/src/graph/automata.png "automata.png")
