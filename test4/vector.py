class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vector):
        return(self.x + vector.x, self.y + vector.y)

    def __mul__(self, n):
        return(self.x * n, self.y * n)

    def __rmul__(self, n):
        return(self.x * n, self.y * n)


v1 = vector(2, 2)
v2 = vector(2, 2)

print(v1 + v2)
print(v1 * 3)
print(4 * v1)
