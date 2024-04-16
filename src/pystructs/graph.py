from typing import Any, Set, Dict, Optional, Tuple, List
from math import inf
from queues import Queue
from linked_list import LinkedList


class Vertex(object):
    value: Any
    colour: Optional[str]
    distance: Optional[int | float]
    parent: Optional['Vertex']
    finish_time: Optional[int]

    def __init__(self, value: Any) -> None:
        self.value = value
        self.colour = None
        self.distance = None
        self.parent = None
        self.finish_time = None

    def __str__(self) -> str:
        return f"Vertex: {self.value}"


class Graph:
    vertices: Dict[Any, Vertex]
    edges: Set[Tuple[Vertex, Vertex]]
    adj: Dict[Vertex, Set[Vertex]]

    directed: bool
    weighted: bool

    _has_cycle: bool

    def __init__(self, directed: bool = False, weighted: bool = False) -> None:

        self.vertices = {}
        self.edges = set()
        self.adj = {}
        self.directed = directed
        self.weighted = weighted
        self._has_cycle = False

    def __str__(self) -> str:
        return_string = ''
        for vertex in self.adj:
            return_string += f"{str(vertex.value)}: "
            for u in self.adj[vertex]:
                return_string += str(u.value) + " "
            return_string += '\n'

        return return_string

    def add_vertex(self, value: Any) -> None:
        self.vertices[value] = Vertex(value)
        self.adj[self.vertices[value]] = set()

    def add_edge(self, v: Any, u: Any, weight: int | float = 1) -> None:
        v = self.vertices[v]
        u = self.vertices[u]
        self.edges.add((v, u))

        if self.directed:
            self.adj[v].add(u)
        else:
            self.adj[v].add(u)
            self.adj[u].add(v)

    def bfs(self, source: Any) -> None:
        for vertex in self.vertices.values():
            vertex.colour = 'white'
            vertex.distance = inf
            vertex.parent = None

        queue = Queue()
        self.vertices[source].colour = 'gray'
        self.vertices[source].distance = 0

        queue.enqueue(self.vertices[source])
        while not queue.is_empty():
            u = queue.dequeue()
            for vertex in self.adj[u]:
                if vertex.colour == 'white':
                    vertex.colour = 'gray'
                    vertex.distance = u.distance + 1
                    vertex.parent = u
                    queue.enqueue(vertex)

            u.colour = 'black'

    def dfs(self, topological_sort: bool = False) -> Optional[LinkedList]:
        self._has_cycle = False
        for vertex in self.vertices.values():
            vertex.colour = 'white'
            vertex.parent = None

        if topological_sort:
            topological_order = LinkedList()

        def _dfs_visit(source: Vertex, time: int):
            time += 1
            source.distance = time
            source.colour = 'gray'
            for v in self.adj[source]:
                if v.colour == 'white':
                    v.parent = source
                    _dfs_visit(v, time)
                if v.colour == 'gray':
                    self._has_cycle = True
            source.colour = 'black'
            time += 1
            source.finish_time = time
            if topological_sort:
                topological_order.insert(0, source.value)
            return

        for vertex in self.vertices.values():
            if vertex.colour == 'white':
                _dfs_visit(vertex, 0)

        if topological_sort and self._has_cycle:
            return LinkedList()
        elif topological_sort:
            return topological_order

    def has_cycle(self):
        self.dfs()
        return self._has_cycle

    def topological_sort(self) -> LinkedList:
        topological_order = self.dfs(topological_sort=True)
        return topological_order

    def is_bipartite(self) -> bool:
        if len(self.vertices) == 0:
            return True

        vertex = None
        for vertex in self.vertices:
            break
        self.bfs(vertex)
        for edge in self.edges:
            if edge[0].distance == edge[1].distance:
                return False
        return True

    def print_tree(self):
        pass