from linked_list import LinkedList as ll
from heaps import MaxHeap as mh
from graph import Graph
from random import shuffle

h = Graph()
for i in range(4):
    h.add_vertex(i + 1)
h.add_edge(1, 2)
h.add_edge(3, 2)
h.add_edge(3, 4)
h.add_edge(1, 4)
h.add_edge(2, 4)



clothes = ['underwear', 'pants', 'belt', 'socks', 'shoes', 'watch', 'shirt', 'tie', 'jacket']
shuffle(clothes)
g = Graph(True, False)

for clothing in clothes:
    g.add_vertex(clothing)

g.add_edge('pants', 'shoes')
g.add_edge('shirt', 'tie')
g.add_edge('underwear', 'pants')
g.add_edge('pants', 'belt')
g.add_edge('belt', 'jacket')
g.add_edge('shirt', 'belt')
g.add_edge('underwear', 'shoes')
g.add_edge('tie', 'jacket')
g.add_edge('socks', 'shoes')


t = g.topological_sort()
print(t)


