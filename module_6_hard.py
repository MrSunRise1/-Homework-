#Практическое задание по модулю: "Наследование классов."
import math
class Figure:
    def __init__(self, color , *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = False
        self.sides_count = 0

        self.set_sides(*sides)

    def __is_valid_color(self, r , g ,b):
        return all(0 <= x <= 255 for x in (r , g , b))

    def get_color(self):
            return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 1
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] if self.get_sides() else 1

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = self.get_sides()[0] if self.get_sides() else 1


class Triangle(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 3
        super().__init__(color, *sides)

    def get_square(self):
        if len(self.get_sides()) < 3:
            return 0
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 12
        super().__init__(color, *sides)
        if not self.get_sides():
            self.set_sides(1)  # Устанавливаем 1, если côtés не заданы
        elif len(self.get_sides()) != 12:
            side_length = self.get_sides()[0]
            self.set_sides(*(side_length for _ in range(12)))

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            super().set_sides(*(new_sides[0] for _ in range(12)))
        else:
            super().set_sides(*([1] * 12))

    def get_volume(self):
        return self.get_sides()[0] ** 3 if self.get_sides() else 1
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(cube1.get_volume())
print(len(circle1))
print(cube1.get_volume())
















