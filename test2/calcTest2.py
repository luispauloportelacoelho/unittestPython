from unittest import TestCase, main
from decimal import Decimal

class Calc:
    def __init__(self):
        self.cache = 0

    def sum_value(self, x, y=None):
        if isinstance(x, int) and isinstance(y, int):
            self.cache = x + y
            return self.cache
        elif y is None:
            return x + self.cache
        else:
            raise Exception('Insert only numbers')

    def sub_value(self, x, y=None):
        if y is None:
            self.cache = x - self.cache
        else:
            self.cache = x - y
            return self.cache

    def mul_value(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            return x * y
        else:
            raise Exception('Insert only numbers')

    def div_value(self, x, y):
        return x / y

    def clear_cache(self):
        self.cache = 0


class test_calc(TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_sum(self):
        self.calc.clear_cache()
        self.assertEqual(self.calc.sum_value(2, 2), 4)

    def test_sum_neg(self):
        self.calc.clear_cache()
        self.assertEqual(self.calc.sum_value(-2, -3), -5)

    #def test_sum_float(self):
    #    self.assertEqual(self.calc.sum_value(2.0, 3.0), 5.0)

    def test_sub(self):
        self.calc.clear_cache()
        self.assertEqual(self.calc.sub_value(2, 2), 0)

    def test_sub_float(self):
        self.calc.clear_cache()
        self.assertEqual(self.calc.sub_value(2.0, 2.0), 0)

    def test_sum_string(self):
        self.calc.clear_cache()
        with self.assertRaises(Exception):
            self.calc.sum_value('Luis', 'Coelho')

    def test_sub_string(self):
        self.calc.clear_cache()
        with self.assertRaises(Exception):
            self.calc.sub_value('Luis', 'Coelho')

    def test_mul(self):
        self.calc.clear_cache()
        self.assertEqual(self.calc.mul_value(3, 3), 9)

    def test_mul_string(self):
        self.calc.clear_cache()
        with self.assertRaises(Exception):
            self.calc.mul_value(3, 'Coelho')

    def test_div(self):
        self.calc.clear_cache()
        self.assertEqual(self.calc.div_value(3, 3), 1)

    def test_div_string(self):
        self.calc.clear_cache()
        with self.assertRaises(Exception):
            self.calc.div_value(3, 'Coelho')

    def test_cache_sum(self):
        self.calc.clear_cache()
        self.assertEqual(self.calc.sum_value(self.calc.sum_value(2, 2)), 8)

    '''def test_cache_sub(self):
        """
        Explanation

        In the first substraction 10 - 5 the result is 5

        cache - result == 0
        """
        self.calc.clear_cache()
        self.assertEqual(self.calc.sub_value(self.calc.sum_value(10, 5)), 0)'''

if __name__ == '__main__':
    main()
