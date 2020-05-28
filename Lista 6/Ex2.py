from math import sqrt


class Ponto:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y


class Triangulo:
    p1 = Ponto(0, 0)
    p2 = Ponto(0, 0)
    p3 = Ponto(0, 0)

    def __init__(self, p1, p2, p3):
        Ponto.__p1 = p1
        Ponto.__p2 = p2
        Ponto.__p3 = p3

    def get_p1(self):
        g = []
        g.append(self.p1.get_x())
        g.append(self.p1.get_y())
        return g

    def get_p2(self):
        g = []
        g.append(self.p2.get_x())
        g.append(self.p2.get_y())
        return g


    def get_p3(self):
        g = []
        g.append(self.p3.get_x())
        g.append(self.p3.get_y())
        return g


def DistanciaTotal(a, b):
    d = sqrt((a ** 2) + (b ** 2))
    return d


def GetPerimetro(triangulo):
    d_p1_p2_x = abs(triangulo.p1.x - triangulo.p2.x)
    d_p1_p2_y = abs(triangulo.p1.y - triangulo.p2.y)
    d_p1_p2 = DistanciaTotal(d_p1_p2_x, d_p1_p2_y)
    d_p1_p3_x = abs(triangulo.p1.x - triangulo.p3.x)
    d_p1_p3_y = abs(triangulo.p1.y - triangulo.p3.y)
    d_p1_p3 = DistanciaTotal(d_p1_p3_x, d_p1_p3_y)
    d_p2_p3_x = abs(triangulo.p2.x - triangulo.p3.x)
    d_p2_p3_y = abs(triangulo.p2.y - triangulo.p3.y)
    d_p2_p3 = DistanciaTotal(d_p2_p3_x, d_p2_p3_y)

    per = d_p1_p2 + d_p1_p3 + d_p2_p3

    return per



def GetInfo():
    tr = Ponto(0, 0)
    tr.set_x(int(input()))
    tr.set_y(int(input()))

    return tr


triangulo = Triangulo(0, 0, 0)
triangulo.p1.set_x(float(input()))
triangulo.p1.set_y(float(input()))
triangulo.p2.set_x(float(input()))
triangulo.p2.set_y(float(input()))
triangulo.p3.set_x(float(input()))
triangulo.p3.set_y(float(input()))

perimetro = GetPerimetro(triangulo)

print("%.2f" % perimetro)
