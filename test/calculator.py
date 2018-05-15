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

    #def test_sum_error(self):
    #    self.assertEquals(sum_values(5,5), 11, msg=None)

    def test_sub(self):
        self.assertEqual(sub_values(5, 5), 0, msg=None)

    def test_mul(self):
        self.assertEqual(mul_values(5, 5), 25, msg=None)


if __name__ == '__main__':
    main()

#test sum_values
#assert sum_values(5, 5) == 10, 'Sum error {}'.format(sum_values(5,5))

#test sub_values
#assert sub_values(4, 5) == -1, 'Sub error {}'.format(sub_values(5,5))

#test mul_values
#assert mul_values(5, 5) == 25, 'Multiplication error {}'.format(sub_values(5,5))
