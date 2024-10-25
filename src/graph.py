import graphviz
import os
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, u, v):
        if u in self.graph and v in self.graph:
            self.graph[u].append(v)
<<<<<<< HEAD
            self.graph[v].append(u)  # Agregar arista no dirigida

    def bfs(self, start):
=======
            self.graph[v].append(u)  

    def bfs(self, start):

>>>>>>> 0d4fafd442ee22948277ef41cd7a6366e9821b7b
        visited = set()
        queue = deque([start])
        bfs_order = []
        bfs_edges = []  # Para almacenar las aristas recorridas

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                bfs_order.append(vertex)
                # Agregar las aristas recorridas
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        bfs_edges.append((vertex, neighbor))  # Almacenar arista
                        queue.append(neighbor)

        return bfs_order, bfs_edges  # Devolvemos las aristas recorridas

    def dfs(self, start):
<<<<<<< HEAD
=======

>>>>>>> 0d4fafd442ee22948277ef41cd7a6366e9821b7b
        visited = set()
        dfs_order = []
        dfs_edges = []  # Para almacenar las aristas recorridas
        self._dfs_recursive(start, visited, dfs_order, dfs_edges)
        return dfs_order, dfs_edges  # Devolvemos las aristas recorridas

    def _dfs_recursive(self, vertex, visited, dfs_order, dfs_edges):
        visited.add(vertex)
        dfs_order.append(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                dfs_edges.append((vertex, neighbor))  # Almacenar arista
                self._dfs_recursive(neighbor, visited, dfs_order, dfs_edges)

    def render_graph(self, name, result_edges=None):
        dot = graphviz.Graph()

        # Crear los nodos del grafo
        for vertex in self.graph:
            dot.node(vertex)
        
        # Crear las aristas
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
<<<<<<< HEAD
                # Solo colorear las aristas recorridas si result_edges no es None
                if result_edges and ((vertex, neighbor) in result_edges or (neighbor, vertex) in result_edges):
                    dot.edge(vertex, neighbor, color="red")  # Resaltar las aristas recorridas
                else:
                    dot.edge(vertex, neighbor)  # Arista sin resaltar

        # Guardar la imagen en el directorio assets
=======
                dot.edge(vertex, neighbor)  

        if result:
            for node in result:
                dot.node(node, color="red") 


>>>>>>> 0d4fafd442ee22948277ef41cd7a6366e9821b7b
        output_path = os.path.join("C:\\Users\\usuario\\Desktop\\MPC2\\assets", f"{name}.png")
        dot.render(output_path.split('.png')[0], format="png")
