import RabinKarp
import unittest

class Test(unittest.TestCase):
    def test_RabinCarp(self):
        pattern = "test"
        with open("test.txt", encoding="utf-8") as file_read:
            main_text = file_read.read()

        self.assertEqual(RabinKarp.search_patterns_in_text(main_text, pattern), 5)
