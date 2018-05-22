"""
1 - function 'nomeadas' (def)
2 - function 'anónima' (lambda)
3 - function class (class)
"""


def sum_values(x, y):
    """Sum two values."""
    return x + y


anonimous_sum = lambda x, y: x + y


class class_sum:
    """e."""

    def __init__(self, x, y):
        """It is like a constructor."""

        self.x = x
        self.y = y

    def __call__(self):
        return self.x + self.y
        
