import pytest
from TarjansAlgo import Graph

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 2)

def test_scc(capsys):
    g.SCC()
    captured = capsys.readouterr()
    assert captured.out == '[1]\n[3, 2, 0]\n'