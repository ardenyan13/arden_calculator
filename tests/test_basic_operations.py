import unittest
from calculator import add, subtract, multiply, divide

class TestBasicOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 7), 17)

    def test_subtract(self):
        self.assertEqual(subtract(10, 2), 8)

    def test_multiple(self):
        self.assertEqual(multiply(7, 9), 63)
    
    def test_divide(self):
        self.assertEqual(divide(48, 8), 6)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()