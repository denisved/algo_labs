import unittest
import main

arr = [52, 0, 266, -25, 15]
sorted_arr_asc = [1, 2, 3, 4, 5]
sorted_arr_desc = [5, 4, 3, 2, 1]


class Test(unittest.TestCase):

    def test_quick_sort_asc(self):
        main.quicksort(arr, 0, len(arr) - 1, False)
        self.assertEqual(arr, sorted(arr, reverse=False))

    def test_quick_sort_desc(self):
        main.quicksort(arr, 0, len(arr) - 1, True)
        self.assertEqual(arr, sorted(arr, reverse=True))

    def test_asc_asc(self):
        main.quicksort(sorted_arr_asc, 0, len(arr) - 1, False)
        self.assertEqual(sorted_arr_asc, [1, 2, 3, 4, 5])

    def test_asc_desc(self):
        main.quicksort(sorted_arr_asc, 0, len(arr) - 1, True)
        self.assertEqual(sorted_arr_asc, [5, 4, 3, 2, 1])

    def test_desc_desc(self):
        main.quicksort(sorted_arr_desc, 0, len(arr) - 1, True)
        self.assertEqual(sorted_arr_desc, [5, 4, 3, 2, 1])

    def test_desc_asc(self):
        main.quicksort(sorted_arr_desc, 0, len(arr) - 1, False)
        self.assertEqual(sorted_arr_desc, [1, 2, 3, 4, 5])
