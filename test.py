import unittest
from BFS import Graph

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(1, 0)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 2)
g.addEdge(3, 4)
g.addEdge(4, 3)


class Test(unittest.TestCase):
    def test_bfs_check_vertex(self):
        self.assertEqual(g.bfs_check_vertex(0, 2), True)
        self.assertEqual(g.bfs_check_vertex(0, 5), False)

    def test_bfs(self):
        self.assertEqual(g.bfs(0), print(0, 1, 2, 3, 4))
