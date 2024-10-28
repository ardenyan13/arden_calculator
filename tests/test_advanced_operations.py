import unittest
from calculator import power, sqrt, n_root, factorial

class TestAdvancedOperations(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(3, 4), 81)

    def test_sqrt(self):
        self.assertEqual(sqrt(144), 12)

    def test_n_root(self):
        self.assertEqual(n_root(32, 5), 2)
    
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

if __name__ == "__main__":
    unittest.main()