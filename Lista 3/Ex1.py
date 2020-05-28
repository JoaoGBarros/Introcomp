mult = []
v = 1
while True:
    num = int(input())

    if num == 0:
        break
    else:
        mult.append(num)

tam = len(mult)

for i in range(0, tam, 1):
    v = v * mult[i]

print("%d" % v)
