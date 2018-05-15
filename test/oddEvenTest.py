from unittest import TestCase, main
from oddEven import is_even


class Test(TestCase):

    def test_even(self):
        self.assertEqual(is_even(2), True, msg=None)

    def test_odd(self):
        self.assertEqual(is_even(1), False, msg=None)

    def test_string(self):
        self.assertEqual(is_even('string'), False, msg=None)

    def test_even_float(self):
        self.assertEquals(is_even(4.0), True, msg=None)


if __name__ == '__main__':
    main()
