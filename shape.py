class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    '''Создали базовый класс который формирует точку с коррдинатой x и y'''

    def __str__(self):
        return 'Shape cord x={} & y={}'.format(self.x, self.y)

    '''Отображение обьекта при запросе'''


class Point(Shape):
    def __init__(self, x=1, y=2):
        super().__init__(x, y)

    def __str__(self):
        return 'P \ h x={} & y={}'.format(self.x, self.y)


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return 'Circle have cord x={} & y={} and radius={}'.format(self.x, self.y, self.radius)

    def check_point_in_circle(self, point):
        if (point.x - self.x) ** 2 + (point.y - self.y) ** 2 <= self.radius:
            return True
        else:
            return False


circle = Circle(4, 9, 18)
circle1 = Circle(2, 3, 10)
point = Point()
print(Circle.check_point_in_circle(circle, point))
print(Circle.check_point_in_circle(circle1, point))