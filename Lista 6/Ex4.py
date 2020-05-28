from math import sqrt


class Ponto:

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

    def __init__(self):
        self.__p1 = Ponto(0, 0)
        self.__p2 = Ponto(0, 0)
        self.__p3 = Ponto(0, 0)


    def set_p1(self):
        x = float(input())
        y = float(input())

        self.__p1.set_x(x)
        self.__p1.set_y(y)

    def set_p2(self):
        x = float(input())
        y = float(input())

        self.__p2.set_x(x)
        self.__p2.set_y(y)

    def set_p3(self):
        x = float(input())
        y = float(input())

        self.__p3.set_x(x)
        self.__p3.set_y(y)

    def get_p1_x(self):
        return self.__p1.get_x()

    def get_p1_y(self):
        return self.__p1.get_y()

    def get_p2_x(self):
        return self.__p2.get_x()

    def get_p2_y(self):
        return self.__p2.get_y()

    def get_p3_x(self):
        return self.__p3.get_x()

    def get_p3_y(self):
        return self.__p3.get_y()

    def get_p1(self):
        g = []
        g.append(self.__p1.get_x())
        g.append(self.__p1.get_y())
        return g

    def get_p2(self):
        g = []
        g.append(self.__p2.get_x())
        g.append(self.__p2.get_y())
        return g

    def get_p3(self):
        g = []
        g.append(self.__p3.get_x())
        g.append(self.__p3.get_y())
        return g


def TipoTriangulo(a, b, c):
    if a == b and a == c:
        return 'equilatero'

    if a == b and a != c:
        return 'isoceles'

    if a == c and a != b:
        return 'isoceles'

    if b == c and b != a:
        return 'isoceles'

    if a != b and a != c and b != c:
        return 'escaleno'


def VerificaTriangulo(a, b, c):
    if abs(b - c) < a < (b+c):
        if abs(a - c) < b < (a + c):
            if abs(a - b) < c < (a + b):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def DistanciaTotal(a, b):
    d = sqrt((a ** 2) + (b ** 2))
    return d


def GetPerimetro(triangulo):
    # a = distancia p1-p2
    # c = distancia p1-p3
    # b = distancia p2-p3
    tri = 0
    d_p1_p2_x = abs(triangulo.get_p1_x() - triangulo.get_p2_x())
    d_p1_p2_y = abs(triangulo.get_p1_y() - triangulo.get_p2_y())
    a = DistanciaTotal(d_p1_p2_x, d_p1_p2_y)
    d_p1_p3_x = abs(triangulo.get_p1_x() - triangulo.get_p3_x())
    d_p1_p3_y = abs(triangulo.get_p1_y() - triangulo.get_p3_y())
    c = DistanciaTotal(d_p1_p3_x, d_p1_p3_y)
    d_p2_p3_x = abs(triangulo.get_p2_x() - triangulo.get_p3_x())
    d_p2_p3_y = abs(triangulo.get_p2_y() - triangulo.get_p3_y())
    b = DistanciaTotal(d_p2_p3_x, d_p2_p3_y)

    op = int(input())
    perimetro = a + b + c

    if VerificaTriangulo(a, b, c):
        tipo = TipoTriangulo(a, b, c)
        print("Os pontos dados formam um triangulo " + tipo)
        tri = 1
    else:
        print("ERRO! Os pontos dados nao formam um triangulo")

    if op == 1 and tri == 1:
        print("{:.2f}".format(perimetro))
    elif op == 2 and tri == 1:
        semip = perimetro / 2
        area = sqrt(semip * (semip - a) * (semip - b) * (semip - c))
        print("{:.2f}".format(area))


def GetInfo():
    tr = Ponto(0, 0)
    tr.set_x(int(input()))
    tr.set_y(int(input()))

    return tr


triangulo = Triangulo()
triangulo.set_p1()
triangulo.set_p2()
triangulo.set_p3()
GetPerimetro(triangulo)


