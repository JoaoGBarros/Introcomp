def processa_string(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")
    return eh_subsequencia(string1, string2)


def eh_subsequencia(string1, string2):
    cont = 0
    string1 = list(string1)
    string2 = list(string2)
    for i in range(0, len(string2)):
        for j in range(0, (len(string1))):
            if string1[j] == string2[i]:
                cont += 1
                break

    if cont == len(string2):
        return True
    else:
        return False



string1 = input()
string2 = input()
print(processa_string(string1, string2))
