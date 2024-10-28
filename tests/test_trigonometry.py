import unittest
from calculator import sin, cos, tan

class TestTrigonometry(unittest.TestCase):
    def test_sin(self):
        self.assertAlmostEqual(sin(90), 1)
        self.assertAlmostEqual(sin(45), 2 ** 0.5 / 2)

    def test_cos(self):
        self.assertAlmostEqual(cos(90), 0)
        self.assertAlmostEqual(cos(45), 2 ** 0.5 / 2)

    def test_tan(self):
        self.assertEqual(tan(0), 0)
        self.assertAlmostEqual(tan(45), 1)
        with self.assertRaises(ZeroDivisionError):
            tan(90)

if __name__ == "__main__":
    unittest.main()