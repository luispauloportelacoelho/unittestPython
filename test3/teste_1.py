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

    def __call__(self, x, y):
        """Sum two values."""
        return x + y


print(class_sum(2, 2))
