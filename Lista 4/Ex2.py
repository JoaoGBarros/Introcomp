matriz = []

entrada = input()
coluna, linha = entrada.split()
coluna = int(coluna)
linha = int(linha)

for i in range(linha):
    matriz.append([])
    for j in range(coluna):
        matriz[i].append(0)

print(matriz)