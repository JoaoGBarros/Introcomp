temp = float(input())

if temp < 35:
    print("Cheque o hardware")
elif 35 <= temp <= 70:
    print("Temperatura normal")
else:
    print("Superaquecimento!")