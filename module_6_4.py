# Задание "Они все так похожи"

from math import pi, sqrt


class Figure:
    sides_count = 0
    def __init__(self, __color, __sides, filled=0):
        """
        :param __sides: список сторон (целые числа)
        :param __color: список цветов в формате RGB
        :param filled: закрашенный, bool
        """
        self.__color = __color
        self.__sides = __sides
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        valid_color = False
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            valid_color = True
        return valid_color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        valid_sides = True
        if len(args) != 1:
            valid_sides = False
        if not(isinstance(args[0], int)):
            valid_sides = False
        return valid_sides

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimetr = 0
        for i in self.__sides:
            perimetr += i
        return perimetr

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [new_sides[0]]




class Circle (Figure):
    sides_count = 1
    def __init__(self, color, *args):
        sides = []
        if len(args) == 1:
            sides.append(args[0])
            self.__radius = args[0] / (2 * pi)
        else:
            sides.append(1)
            self.__radius = 1 / (2 * pi)
        super().__init__(list(color), sides)


class Triangle (Figure):
    sides_count = 3
    def __init__(self, color, *args):
        self.sides = []
        if len(args) == 1:
            for i in range(self.sides_count):
                self.sides.append(args[0])
        else:
            for i in range(self.sides_count):
                self.sides.append(1)
        super().__init__(list(color), self.sides)

    def get_square(self):
        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[2]
        p = (a + b + c) / 2
        s = sqrt(p*(p-a)*(p-b)*(p-c))
        return round(s, 2)

class Cube (Figure):
    sides_count = 12
    def __init__(self, color, *args):
        self.__sides = []
        if len(args) == 1:
            for i in range(self.sides_count):
                self.__sides.append(args[0])
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)
        super().__init__(list(color), self.__sides)

    def get_volume(self):
        return self.__sides[0]*self.__sides[0]*self.__sides[0]

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())



