#!/usr/bin/python3
""" square class"""


class Square():
    """ Square class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ class"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ perimeter square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ square object """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Square"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
