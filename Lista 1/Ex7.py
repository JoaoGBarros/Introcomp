from math import pi
from math import sqrt

raio = float(input())


area = pi * (raio ** 2)
print("%.2f" % area)

nova_area = area / 2
raio2 = sqrt(nova_area/pi)

print("%.2f" % raio2)
