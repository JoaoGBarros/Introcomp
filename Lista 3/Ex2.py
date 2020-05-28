num = int(input())
lista = []
while True:
    chute = int(input())
    lista.append(chute)
    if chute > num:
        print("Chute alto")
    elif chute < num:
        print("Chute baixo")
    else:
        print("Acertou!")
        print(lista)
        break
