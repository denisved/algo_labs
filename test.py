import unittest
from calendar import merge_ranges


class Test(unittest.TestCase):
    def test_merge_ranges(self):
        meetings = [(0, 2), (1, 4), (3, 5), (6, 7), (8, 9)]
        self.assertEqual(merge_ranges(meetings), [(0, 5), (6, 7), (8, 9)])
        
    def test_one_tuple(self):
        meetings = [(0, 2), (2, 4), (4, 5), (5, 5), (5, 10)]
        self.assertEqual(merge_ranges(meetings), [(0, 10)])

    def test_no_merges(self):
        meetings = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
        self.assertEqual(merge_ranges(meetings), [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)])

    def test_big_tuples(self):
        meetings = [(0, 100), (100, 4000), (50, 4500), (15000, 20000)]
        self.assertEqual(merge_ranges(meetings), [(0, 4500), (15000, 20000)])
