# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def line(self, dot):
        return (
               (self.x - dot.x) ** 2 +
               (self.y - dot.y) ** 2) ** 0.5


    def __str__(self):
        return f"x={self.x}, y={self.y}"


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c


    def istriangle(self):
        """
        Функция определяет, что три точки не лежат на одной прямой.
        НЕ треугольник:
        x1 == x2 == x3  ИЛИ
        y1 == y2 == y3
        :return: true or false
        """
        if self.a.x == self.b.x == self.c.x:
            return False
        elif (self.a.y == self.b.y == self.c.y):
            return False
        else:
            return True

    if Triangle.istriangl:   ##  с такой проверкой не рабтает
        def perimeter(self):
            return (
                a.line(self.b) +
                b.line(self.c) +
                c.line(self.a)
                )

        def area(self):
            p = self.perimeter() / 2
            ab = a.line(b)
            bc = b.line(c)
            ca = c.line(a)
            return str((p * (p - ab) * (p - bc) * (p - ca)) ** 0.5)
    else: pass
    #    return '"Не треугольник'

class Trapeze:
    def __init__(self, a: Point, b: Point, c: Point, d: Point):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def istrapezem(self):
        '''Проверка что это трапеция. точки не лежат на одной прямой,
         две стороны паралльны и две другие - не параллеельны'''
        pass

    def istrapezemirror(self):
        '''GПроверка что трапеция равнобедрренна'''
        pass

    def perimeter(self):
        return (
            a.line(self.b) +
            b.line(self.c) +
            c.line(self.d) +
            d.line(self.a)
            )


##################################################

a = Point()
b = Point(3, 0)
c = Point(3, 4)
triangle = Triangle(a, b, c)

print(str(a))
print(str(b))
print(str(b))
print('ab=', a.line(b), '\nbc=', b.line(c), '\nca=', c.line(a))

print("perimeter", triangle.perimeter())
print("Area", triangle.area())
#########

trapeze = Trapeze(Point(), Point(10,0), Point(8, 6), Point(2,6))

