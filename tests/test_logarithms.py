import unittest
from calculator import log, ln, exponential
import math

class TestLogarithms(unittest.TestCase):
    def test_log(self):
        self.assertEqual(log(100), 2)
        self.assertEqual(log(64, 2), 6)

    def test_ln(self):
        self.assertEqual(ln(1), 0)
        self.assertEqual(ln(math.e), 1)

    def test_exponential(self):
        self.assertEqual(exponential(1), math.e)
        self.assertEqual(exponential(0), 1)

if __name__ == "__main__":
    unittest.main()