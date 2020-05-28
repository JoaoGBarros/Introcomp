def eh_palindromo(string1):
    string2 = list(string1)
    string2.reverse()
    st = ''.join(string2)

    if string1 == st:
        return True
    else:
        return False


string1 = input()
print(eh_palindromo(string1))