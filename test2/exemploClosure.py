def external(func):
    print(func)
    def internal(x, y):
        func(x, y)

    return internal


@external
def sum_value2(x, y):
    return x + y


print(sum_value2(2, 2))
#is the same as
#print(external(sum_value2(2, 2)))
