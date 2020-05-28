def inverte_string(string1):
    st = list(string1)
    st.reverse()
    return ''.join(st)



string1 = input()
print(inverte_string(string1))

