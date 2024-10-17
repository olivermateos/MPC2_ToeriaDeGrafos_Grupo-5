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
            self.graph[v].append(u)  

    def bfs(self, start):

        visited = set()
        queue = deque([start])
        bfs_order = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                bfs_order.append(vertex)
                queue.extend([neighbor for neighbor in self.graph[vertex] if neighbor not in visited])

        return bfs_order

    def dfs(self, start):

        visited = set()
        dfs_order = []
        self._dfs_recursive(start, visited, dfs_order)
        return dfs_order

    def _dfs_recursive(self, vertex, visited, dfs_order):
        visited.add(vertex)
        dfs_order.append(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited, dfs_order)

    def render_graph(self, name, result=None):
        dot = graphviz.Graph()
        for vertex in self.graph:
            dot.node(vertex)
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                dot.edge(vertex, neighbor)  

        if result:
            for node in result:
                dot.node(node, color="red") 


        output_path = os.path.join("C:\\Users\\usuario\\Desktop\\MPC2\\assets", f"{name}.png")
        dot.render(output_path.split('.png')[0], format="png")
