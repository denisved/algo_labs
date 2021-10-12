import unittest
from hash_table import HashTable

hash_table = HashTable()


class Test(unittest.TestCase):
    def test_insert(self):
        hash_table.insert(0, "test")
        self.assertEqual(hash_table.get_table(), [[(0, "test")], [], [], [], [], [], [], [], [], []])

    def test_search(self):
        hash_table.insert(0, "test")
        self.assertEqual(hash_table.search(0), "test")

    def test_delete(self):
        hash_table.insert(0, "test")
        self.assertEqual(hash_table.get_table(), [[(0, "test")], [], [], [], [], [], [], [], [], []])
        hash_table.delete(0)
        self.assertEqual(hash_table.get_table(), [[], [], [], [], [], [], [], [], [], []])
