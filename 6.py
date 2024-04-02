class Point:
    def __init__(self, coordinates: tuple = (0, 0)):
        self.__coordinates = coordinates

    def get_x(self):
        """
        :return: x coordinate
        """
        return self.__coordinates[0]

    def get_y(self):
        """
        :return: y coordinate
        """
        return self.__coordinates[1]

    def distance(self, other: tuple):
        """
        :param other: tuple of enother point
        :return: distance between two points
        """
        x2 = other[0]
        y2 = other[1]
        x1 = self.__coordinates[0]
        y1 = self.__coordinates[1]
        dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
        return dist

    def sum(self, other: tuple):
        """
        :param other: tuple of enother point
        :return: new point with sum of two points
        """
        new_point = (
            self.__coordinates[0] + other[0],
            self.__coordinates[1] + other[1]
        )
        return new_point

    def __str__(self):
        return self.__coordinates


p = Point((1, 1))
print(p.get_x())
print(p.get_y())
print(p.distance((10, 10)))
print(p.sum((5, 5)))
print(p.__str__())
