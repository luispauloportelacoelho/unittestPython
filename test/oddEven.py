from unittest import TestCase, main
"""
The function verify if a number is even
"""


def is_even(number: int) -> bool:
    try:
        if (number % 2) == 0:
            return True
        else:
            return False
    except TypeError:
        return False


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
