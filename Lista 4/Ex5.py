matriz1 = []
matriz2 = []
matriz_final = []
valor = 0
k = 0

num = list(map(int, input().split()))
for i in range(0, 3, 1):
    matriz1.append([])
    for j in range(0, 3, 1):
        matriz1[i].append(num[k])
        k += 1

k = 0

num = list(map(int, input().split()))
for i in range(0, 3, 1):
    matriz2.append([])
    for j in range(0, 3, 1):
        matriz2[i].append(num[k])
        k += 1


for i in range(3):
    matriz_final.append([])
    for j in range(3):
        valor = 0
        for o in range(3):
            valor = valor + (matriz1[i][o] * matriz2[o][j])
        matriz_final[i].append(valor)


print(matriz_final)