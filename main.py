class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start_vertex):
        visited = [False] * self.vertices
        traversal_order = []
        self.dfs_helper(start_vertex, visited, traversal_order)
        return traversal_order

    def dfs_helper(self, vertex, visited, traversal_order):
        visited[vertex] = True
        traversal_order.append(vertex)
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs_helper(neighbor, visited, traversal_order)

    def bfs(self, start_vertex):
        visited = [False] * self.vertices
        traversal_order = []
        queue = [start_vertex]
        visited[start_vertex] = True
        while queue:
            vertex = queue.pop(0)
            traversal_order.append(vertex)
            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        return traversal_order

graph = Graph(7)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
print(graph.dfs(0))
print(graph.bfs(0))