import main
import unittest

class Test(unittest.TestCase):
    def test_wchain(self):
        self.assertEqual(main.wchain(['testt', 'tett', 'tet', 'randomword', 's']), 3)

