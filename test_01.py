import pygraphviz as pgv

#init my graph
G = pgv.AGraph()

#add some nodes
G.add_node(1, color='red')
G.add_edge('b','c',color='blue')

# render
G.layout()
G.draw('test_01.png')
