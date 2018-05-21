"""Function 'nomeadas'."""


def sum_values(x, y):
    """Sum two values."""
    return x + y


def div_values(x, y):
    """Divide two values."""
    return x / y


"""Lambda function."""
sum_values2 = lambda x: x + 2


class class_sum:
    """Class for sum."""
    def __init__(self, x, y):
        """Initalize values."""
        self.x = x
        self.y = y

    def __call__(self):
        """Sum two values."""
        return self.x + self.y

a = class_sum(2, 2)
print(a())
