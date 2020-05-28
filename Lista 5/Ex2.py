def no_intervalo(lim1,lim2,num):
    if lim1 <= num <= lim2:
        return True
    else:
        return False



lim1 = int(input())
lim2 = int(input())
num = int(input())

print(no_intervalo(lim1, lim2, num))