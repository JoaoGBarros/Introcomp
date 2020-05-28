num = int(input())
print(num)
while num != 1:

    if num % 2 == 1:
        num = (num * 3) + 1
    else:
        num = num / 2
    print("%d" % num)
