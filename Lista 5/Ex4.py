def processa_string(string1):
    string1 = string1.lower()
    string1 = string1.replace(" ", "")
    return eh_palindromo(string1)

def eh_palindromo(string1):
    string_reversa = list(string1)
    string_reversa.reverse()
    st = ''.join(string_reversa)

    if string1 == st:
        return True
    else:
        return False

string1 = input()
print(processa_string(string1))