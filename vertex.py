class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}
    
    def add_edge(self, vertex_v, weight = 0):
        self.edges[vertex_v] = weight

    def get_edges(self):
        return list(self.edges.keys())