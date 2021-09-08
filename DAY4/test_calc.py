import unittest
import unittestingcalc as calc
from parameterized import parameterized


class TestCalc(unittest.TestCase):

    @parameterized.expand([
        [10,15,25],
        [-8,-3,-11],
        [-4,7,3],
    ])
    def test_add(self,a,b,c):
        self.assertEqual(calc.add(a,b),c)

    @parameterized.expand([
        [10, 15, -5],
        [-8, -3, -5],
        [-4, 0, -4],
    ])
    def test_subtract(self, a, b, c):
        self.assertEqual(calc.subtract(a, b), c)

    @parameterized.expand([
        [10, 5, 50],
        [-8, -3, 24],
        [-4, 7, -28],
    ])
    def test_multiply(self, a, b, c):
        self.assertEqual(calc.multiply(a, b), c)

    @parameterized.expand([
        [-10, 5, -2],
        [7, 10, 0.7],
        [4, 2, 2],
    ])
    def test_divide(self, a, b, c):
        if b==0:
            self.assertRaises(ValueError,calc.divide,a,b)
        self.assertEqual(calc.divide(a, b), c)
