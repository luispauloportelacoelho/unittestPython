from unittest import TestCase, main


def sum_values(x, y):
    return x + y


def sub_values(x, y):
    return x - y


def mul_values(x, y):
    return x * y

class Tests(TestCase):
    def test_sum(self):
        self.assertEqual(sum_values(5, 5), 10, msg=None)

    def test_sub(self):
        self.assertEqual(sub_values(5, 5), 0, msg=None)

    def test_mul(self):
        self.assertEqual(mul_values(5, 5), 25, msg=None)

if __name__ == '__main__':
    main()
