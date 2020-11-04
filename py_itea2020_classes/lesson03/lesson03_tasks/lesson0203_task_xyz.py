class Point:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def setX(self, x):
        self._x = x

    def getX(self):
        return self._x

    def setY(self, y):
        self._y = y

    def getY(self):
        return self._y

    def setZ(self, z):
        self._z = z

    def getZ(self):
        return self._z

    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y, self._z + other._z)

    def __sub__(self, other):
        return Point(self._x - other._x, self._y - other._y, self._z - other._z)

    def __mul__(self, other):
        return Point(self._x * other._x, self._y * other._y, self._z * other._z)

    def __truediv__(self, other):
        return Point(self._x / other._x, self._y / other._y, self._z / other._z)

    def __neg__(self):
        return Point(-self._x, -self._y, -self._z)

    def __str__(self):
        return f'X: {self._x}, Y: {self._y}, Z: {self._z}'

point1 = Point (1, 2, 3)
point2 = Point(1, 2, 3)
point3 = point1*point2
print(point3)