var = 7


def func():
    """Print a variable."""

    global var
    print(var)
    var = 18
    print(var)


func()
print(func())
