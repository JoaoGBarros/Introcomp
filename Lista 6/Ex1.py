from math import *


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


def Dist(p1, p2):
    distancia_x = abs(p1.x - p2.x)
    distancia_y = abs(p1.y - p2.y)
    distancia_total = sqrt((distancia_x ** 2) + (distancia_y ** 2))
    return distancia_total


p1 = Ponto(0, 0)
p2 = Ponto(0, 0)
p1.set_x(float(input()))
p1.set_y(float(input()))
p2.set_x(float(input()))
p2.set_y(float(input()))
distancia = Dist(p1, p2)
print("%.2f" % distancia)
