from vertex import Vertex

class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        if from_vertex.value in self.graph_dict and to_vertex in self.graph_dict:
            self.graph_dict[from_vertex.value].add_edge(to_vertex, weight)
            self.graph_dict[to_vertex.value].add_edge(from_vertex, weight)