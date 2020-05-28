unidade = input()
temp = float(input())


if unidade == 'C':
    conv = (temp * 1.8) + 32
elif unidade == 'F':
    conv = (temp - 32) / 1.8

print("%.1f" % conv)