matriz = []
k = 0
num = list(map(int, input().split()))
for i in range(0, 3, 1):
    matriz.append([])
    for j in range(0, 3, 1):
        matriz[i].append(num[k])
        k+=1

print(matriz)
