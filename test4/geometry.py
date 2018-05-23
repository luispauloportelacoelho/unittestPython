class Point:
    """Create point."""
    def __init__(self, x, y):
        """Initialize."""
        self.x = x
        self.y = y

    def __repr__(self):
        """Representation."""
        return 'Point({}, {})'.format(self.x,
                                      self.y)


class line:
    """Create line."""
    def __init__(self, p_1, p_2):
        """Initialize line."""
        self.point_1 = p_1
        self.point_2 = p_2

    @property
    def distancia_x(self):
        """Calculate distante in x."""
        return abs(self.point_2.x - self.point_1.x)

    @property
    def distancia_y(self):
        """Calculate distante in y."""
        return abs(self.point_2.y - self.point_1.y)

    def __repr__(self):
        """Line representation."""
        return 'line([{}, {}])'.format(self.point_1, self.point_2)


point_1 = Point(5, 2)
point_2 = Point(1, 5)

line_x = line(point_1, point_2)
print(line_x.distancia_x())
# point_3 = point(4, 7)
#
# print(point_1)
# print(point_2)
# print(point_3)

# line_1 = line(point_1, point_2)
#
# print(line_1.distancia_x)
# print(line_1.distancia_y)
# print(line_1)
