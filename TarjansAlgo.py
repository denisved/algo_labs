from collections import defaultdict


class Graph:
    def __init__(self, vertexNumber):
        self.vertex = vertexNumber
        self.graph = defaultdict(list)
        self.id = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def Tarjan(self, u, lowLinks, stack, stackMember, discoveredIds):

        discoveredIds[u] = self.id
        lowLinks[u] = self.id
        self.id += 1
        stackMember[u] = True
        stack.append(u)

        for currentVertex in self.graph[u]:
            if discoveredIds[currentVertex] == -1:
                self.Tarjan(currentVertex, lowLinks, stack, stackMember, discoveredIds)
                lowLinks[u] = min(lowLinks[u], lowLinks[currentVertex])

            elif stackMember[currentVertex] == True:
                lowLinks[u] = min(lowLinks[u], discoveredIds[currentVertex])


        extractedVertex = -1
        ssc_array = []


        if lowLinks[u] == discoveredIds[u]:
            while extractedVertex != u:
                extractedVertex = stack.pop()
                ssc_array.append(extractedVertex)
                stackMember[extractedVertex] = False
            print(ssc_array)

    def SCC(self):
        discoverIds = [-1] * (self.vertex)
        lowLinks = [-1] * (self.vertex)
        stackMember = [False] * (self.vertex)
        stack = []

        for i in range(self.vertex):
            if discoverIds[i] == -1:
                self.Tarjan(i, lowLinks, stack, stackMember, discoverIds)

if __name__ == '__main__':
    g = Graph(7)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 2)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    g.addEdge(6, 4)

    print("SSC in graph according to Tarjan's algorithm")
    g.SCC()