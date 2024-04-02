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
        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
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
        """
        :return: Coordinates
        """
        return self.__coordinates


class Segment:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1.__str__()
        self.point2 = point2.__str__()

        self.one_intersection = self.__intersection_identifier(self.point1, self.point2)

    def __intersection_identifier(self, point1, point2):
        point1_sector = self.__sector_identifier(point1)
        point2_sector = self.__sector_identifier(point2)

        if abs(point1_sector - point2_sector) == 1:
            return True
        return False

    def __sector_identifier(self, point):
        x = point[0]
        y = point[1]
        if 0 < x and 0 < y:
            return 1
        if x < 0 < y:
            return 2
        if x < 0 and y < 0:
            return 3
        if x > 0 > y:
            return 4


class CoordinateSystem:
    def __init__(self):
        self.segments = []

    def add_segment(self, segment: Segment):
        """
        :param segment: Segment
        :return: None
        """
        self.segments.append(segment)

    def axis_intersection(self):
        """
        :return: Sum of segments
        """
        return sum(segment.one_intersection for segment in self.segments)


p1 = Point((-10, 10))
p2 = Point((3, 8))
s = Segment(p1, p2)
print(s.one_intersection)
cs = CoordinateSystem()
cs.add_segment(s)
print(cs.axis_intersection())
