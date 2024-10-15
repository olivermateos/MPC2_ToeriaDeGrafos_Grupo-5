import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from graph import Graph  # Importa la clase Graph del archivo graph.py

# Definir el directorio donde se guardarán las imágenes
ASSETS_DIR = "C:\\Users\\usuario\\Desktop\\MPC2\\assets"

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Grafos - BFS & DFS")
        self.graph = Graph()

        # Crear el directorio de assets si no existe
        if not os.path.exists(ASSETS_DIR):
            os.makedirs(ASSETS_DIR)

        # Variables para la interfaz
        self.vertex_entry = tk.Entry(self.root)
        self.edge_entry = tk.Entry(self.root)
        self.vertex_listbox = tk.Listbox(self.root, height=6)  # Lista para mostrar vértices agregados
        self.edge_listbox = tk.Listbox(self.root, height=6)    # Lista para mostrar aristas agregadas

        # Estructura básica de la GUI
        self.setup_ui()

    def setup_ui(self):
        # Sección de ingreso de vértices y aristas
        tk.Label(self.root, text="Vértice:").grid(row=0, column=0)
        self.vertex_entry.grid(row=0, column=1)
        tk.Button(self.root, text="Agregar Vértice", command=self.add_vertex).grid(row=0, column=2)

        tk.Label(self.root, text="Arista (formato: A-B):").grid(row=1, column=0)
        self.edge_entry.grid(row=1, column=1)
        tk.Button(self.root, text="Agregar Arista", command=self.add_edge).grid(row=1, column=2)

        tk.Button(self.root, text="Generar Grafo", command=self.render_graph).grid(row=2, column=1)

        # Mostrar vértices y aristas agregadas
        tk.Label(self.root, text="Vértices Agregados:").grid(row=3, column=0)
        self.vertex_listbox.grid(row=4, column=0)

        tk.Label(self.root, text="Aristas Agregadas:").grid(row=3, column=1)
        self.edge_listbox.grid(row=4, column=1)

        # Área para visualizar el grafo original
        tk.Label(self.root, text="Grafo Original:").grid(row=5, column=0)
        self.original_canvas = tk.Label(self.root)
        self.original_canvas.grid(row=6, column=0, columnspan=3)

        # Botones para ejecutar BFS y DFS
        tk.Button(self.root, text="Ejecutar BFS", command=self.run_bfs).grid(row=7, column=0)
        tk.Button(self.root, text="Ejecutar DFS", command=self.run_dfs).grid(row=7, column=2)

        # Área para visualizar el grafo resultante de BFS o DFS
        tk.Label(self.root, text="Grafo BFS:").grid(row=8, column=0)
        self.bfs_canvas = tk.Label(self.root)
        self.bfs_canvas.grid(row=9, column=0, columnspan=3)

        tk.Label(self.root, text="Grafo DFS:").grid(row=10, column=0)
        self.dfs_canvas = tk.Label(self.root)
        self.dfs_canvas.grid(row=11, column=0, columnspan=3)

    def add_vertex(self):
        vertex = self.vertex_entry.get()
        if vertex:
            self.graph.add_vertex(vertex)
            self.vertex_listbox.insert(tk.END, vertex)  # Mostrar el vértice en la lista
            messagebox.showinfo("Éxito", f"Vértice {vertex} agregado.")
        else:
            messagebox.showerror("Error", "Debe ingresar un vértice.")

    def add_edge(self):
        edge = self.edge_entry.get()
        try:
            u, v = edge.split('-')
            self.graph.add_edge(u.strip(), v.strip())
            self.edge_listbox.insert(tk.END, f"{u} -- {v}")  # Mostrar la arista en la lista
            messagebox.showinfo("Éxito", f"Arista {u} -- {v} agregada.")
        except ValueError:
            messagebox.showerror("Error", "Formato incorrecto. Use A-B.")

    def render_graph(self):
        # Genera el grafo original
        self.graph.render_graph('original')
        self.show_image(os.path.join(ASSETS_DIR, 'original.png'), self.original_canvas)

    def run_bfs(self):
        start_vertex = self.vertex_entry.get()
        if start_vertex not in self.graph.graph:
            messagebox.showerror("Error", "Vértice no encontrado.")
            return
        bfs_result = self.graph.bfs(start_vertex)
        self.graph.render_graph('bfs', bfs_result)
        self.show_image(os.path.join(ASSETS_DIR, 'bfs.png'), self.bfs_canvas)

    def run_dfs(self):
        start_vertex = self.vertex_entry.get()
        if start_vertex not in self.graph.graph:
            messagebox.showerror("Error", "Vértice no encontrado.")
            return
        dfs_result = self.graph.dfs(start_vertex)
        self.graph.render_graph('dfs', dfs_result)
        self.show_image(os.path.join(ASSETS_DIR, 'dfs.png'), self.dfs_canvas)

    def show_image(self, image_path, canvas):
        # Muestra la imagen generada en la interfaz gráfica
        if os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize((400, 300), Image.Resampling.LANCZOS)  # Reemplazamos ANTIALIAS con LANCZOS
            img_tk = ImageTk.PhotoImage(img)
            canvas.config(image=img_tk)
            canvas.image = img_tk

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()  # Esto es crucial para que la ventana se muestre
