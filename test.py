import unittest
from calendar import merge_ranges


class Test(unittest.TestCase):
    def test_merge_ranges(self):
        meetings = [(0, 2), (1, 4), (3, 5), (6, 7), (8, 9)]
        self.assertEqual(merge_ranges(meetings), [(0, 5), (6, 7), (8, 9)])
