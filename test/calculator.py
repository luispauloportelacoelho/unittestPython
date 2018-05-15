def sum_values(x, y):
    return x + y

def sub_values(x, y):
    return x - y

def mul_values(x, y):
    return x * y

#test sum_values
assert sum_values(5, 5) == 10, 'Sum error {}'.format(sum_values(5,5))

#test sub_values
assert sub_values(4, 5) == -1, 'Sub error {}'.format(sub_values(5,5))

#test mul_values
assert mul_values(5, 5) == 25, 'Multiplication error {}'.format(sub_values(5,5))
