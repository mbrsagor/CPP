class Point:
    """Represents a point in 2-D space."""


blank = Point()
blank.x = 3.0
blank.y = 4.0

xy = '(%g, %g)' % (blank.x, blank.y)
print(xy)


def print_point(p):
    print('(%g, %g)' % (p.x, p.y))


class Rectangle(object):
    """Represents a rectangle.
    attributes: width, height, corner.
    """


box = Rectangle()
box.width = 100.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2
    p.y = rect.corner.y + rect.height / 2
    return p


# center = find_center(box)

