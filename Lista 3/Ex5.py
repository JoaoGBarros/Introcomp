tam = int(input())
fibo = [0, 1]
for i in range(0, tam - 2, 1):
    result = fibo[i] + fibo[i+1]
    fibo.append(result)

print(fibo)
