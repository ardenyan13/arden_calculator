import unittest
from calculator import mean, median, mode, standard_deviation

class TestStatistics(unittest.TestCase):
    def test_mean(self):
        self.assertAlmostEqual(mean([4, 6, 5]), 5)
        with self.assertRaises(ZeroDivisionError):
            mean([])

    def test_median(self):
        self.assertEqual(median([5, 5, 2, 1, 4]), 4)

    def test_mode(self):
        self.assertEqual(mode([1, 1, 3, 3, 3, 4, 5]), 3)
    
    def test_standard_deviation(self):
        self.assertAlmostEqual(standard_deviation([1, 1, 1, 1]), 0)
        self.assertAlmostEqual(standard_deviation([1, 2, 3, 4, 5]), 1.4142135623730951)

if __name__ == "__main__":
    unittest.main()