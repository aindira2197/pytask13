class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def dfs(self, vertex):
        visited = [False] * self.V
        self._dfs(vertex, visited)

    def _dfs(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=' ')
        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited)

    def bfs(self, vertex):
        visited = [False] * self.V
        queue = []
        queue.append(vertex)
        visited[vertex] = True
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex, end=' ')
            for neighbor in self.adj_list[current_vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

    def print_graph(self):
        for i in range(self.V):
            print(f"Vertex {i} is connected to: {self.adj_list[i]}")

g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

print("Depth First Traversal (starting from vertex 0):")
g.dfs(0)
print("\nBreadth First Traversal (starting from vertex 0):")
g.bfs(0)
print("\nGraph:")
g.print_graph()