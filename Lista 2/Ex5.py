a = float(input())
b = float(input())
c = float(input())

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print("NENHUMA")
elif delta == 0:
    print("UMA")
else:
    print("DUAS")