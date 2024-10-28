import unittest
from calculator import add_complex, subtract_complex, multiply_complex, divide_complex

class TestComplexNumbers(unittest.TestCase):
    def test_add_complex(self):
        self.assertEqual(add_complex(1 + 2j, 1 + 3j), 2 + 5j)

    def test_subtract_complex(self):
        self.assertEqual(subtract_complex(1 + 2j, 1 + 3j), -1j)

    def test_multiply_complex(self):
        self.assertEqual(multiply_complex(1 + 2j, 1 + 3j), -5 + 5j)
    
    def test_divide_complex(self):
        self.assertEqual(divide_complex(1 + 2j, 1 + 2j), 1)
        with self.assertRaises(ZeroDivisionError):
            divide_complex(1 + 2j, 0)

if __name__ == "__main__":
    unittest.main()