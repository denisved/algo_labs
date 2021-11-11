from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = []
        queue = []
        queue.append(start)

        while queue:
            current = queue.pop(0)
            visited.append(current)
            print(current, end=" ")
            for node in self.graph[current]:
                if node not in visited:
                    queue.append(node)

    def bfs_check_vertex(self, start, vertex):
        visited = []
        queue = []
        queue.append(start)

        while queue:
            current = queue.pop(0)
            visited.append(current)
            if vertex == current:
                print("We have found the vertex", vertex)
                return True

            for node in self.graph[current]:
                if node not in visited:
                    queue.append(node)
        return False



if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(3, 2)
    g.addEdge(2, 4)
    g.addEdge(4, 6)
    g.addEdge(0, 0)
    g.addEdge(6, 5)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.bfs(2)

    print("\n\nLet's check if we can find any vertex in the graph")
    g.bfs_check_vertex(0, 6)

