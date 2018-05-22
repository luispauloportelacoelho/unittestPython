"""Simple decorador."""


def decorador(func):
    """Decorador."""
    def interna(x, y):
        if isinstance(x, int) and isinstance(y, int):
            return func(x, y)
        else:
            raise ValueError('Insira somente inteiros')
    return interna


"""decorador -> interna -> função decorada"""


@decorador
def sum_values(x: int, y: int):
    """Sum two values."""
    return x + y


@decorador
def div_values(x: int, y: int):
    """Divide two numbers."""
    return x / y


print(sum_values(2, 2))
print(div_values(3, 'Paulo'))
