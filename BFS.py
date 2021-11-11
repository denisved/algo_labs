from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(start)
        visited[start] = True

        while queue:
            current = queue.pop(0)
            print(current, end=" ")
            for i in self.graph[current]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def bfs_is_path_exists(self, start, end):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(start)
        visited[start] = True

        while queue:
            current = queue.pop(0)
            if current == end:
                print(f"The path between vertex {start} and {end} exists!")
                return True
            for i in self.graph[current]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return False


    def bfs_shortest_path(self, start, end):
        visited = []
        queue = [[start]]
        if start == end:
            print("Same vertices")
            return
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in visited:
                neighbours = self.graph[node]
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == end:
                        print("Shortest path = ", *new_path)
                        return new_path
                visited.append(node)


if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(3, 4)
    g.addEdge(2, 4)
    g.addEdge(4, 4)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.bfs(0)

    print("\n\nLet's check if we can find any path from vertex A to vertex B")
    g.bfs_is_path_exists(0, 4)

    g.bfs_shortest_path(0, 4)
