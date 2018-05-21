from unittest import TestCase, main
from numbers import Number


def validate_apply_cache(func, cache={}):
    def validate(self, x, y=None):
        key = False
        if y == None:
            y = cache['value']
            key = True

        if isinstance(x, Number) and isinstance(y, Number):
            if key:
                cache['value'] = func(self, y, x)
            else:
                cache['value'] = func(self, x, y)

            return cache['value']
        else:
            raise Exception('only numbers')
    return validate


class Calc:
    @validate_apply_cache
    def sum_value(self, x, y=None):
        return x + y

    @validate_apply_cache
    def sub_value(self, x, y=None):
        return x - y

    @validate_apply_cache
    def mul_value(self, x, y):
        return x * y

    @validate_apply_cache
    def div_value(self, x, y):
        return x / y


class test_calc(TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_sum(self):
        self.assertEqual(self.calc.sum_value(2, 2), 4)

    def test_sum_neg(self):
        self.assertEqual(self.calc.sum_value(-2, -3), -5)

    def test_sub(self):
        self.assertEqual(self.calc.sub_value(2, 2), 0)

    def test_sub_float(self):
        self.assertEqual(self.calc.sub_value(2.0, 2.0), 0)

    def test_sum_string(self):
        with self.assertRaises(Exception):
            self.calc.sum_value('Luis', 'Coelho')

    def test_sub_string(self):
        with self.assertRaises(Exception):
            self.calc.sub_value('Luis', 'Coelho')

    def test_mul(self):
        self.assertEqual(self.calc.mul_value(3, 3), 9)

    def test_mul_string(self):
        with self.assertRaises(Exception):
            self.calc.mul_value(3, 'Coelho')

    def test_div(self):
        self.assertEqual(self.calc.div_value(3, 3), 1)

    def test_div_string(self):
        with self.assertRaises(Exception):
            self.calc.div_value(3, 'Coelho')

    def test_cache_sum(self):
        self.assertEqual(self.calc.sum_value(self.calc.sum_value(2, 2)), 8)

    def test_cache_sub(self):
        """
        Explanation

        In the first substraction 10 - 5 the result is 5

        cache - result == 0.
        """
        self.assertEqual(self.calc.sub_value(self.calc.sum_value(10, 5)), 0)

    def test_sub_with_result_neg_mul_cache(self):
        self.assertEqual(self.calc.sub_value(3, 10), -7)
        self.assertEqual(self.calc.mul_value(3), -21)

    def test_sub_with_result_neg_sum_cache(self):
        self.assertEqual(self.calc.sub_value(3, 10), -7)
        self.assertEqual(self.calc.sum_value(3), -4)

    def test_sum_with_result_pos_with_sub_cache(self):
        self.assertEqual(self.calc.sum_value(1, 1), 2)
        self.assertEqual(self.calc.sub_value(3), -1)

if __name__ == '__main__':
    main()
