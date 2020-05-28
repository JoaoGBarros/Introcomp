p1 = float(input())
p2 = float(input())
p3 = float(input())

media = (p1 + p2 + p3) / 3

if media < 7:
    print("Aluno Reprovado!")
elif 7 <= media < 8:
    print("Aluno Aprovado!")
    print("Certificado Bronze")
elif 8 <= media < 9:
    print("Aluno Aprovado!")
    print("Certificado Prata")
else:
    print("Aluno Aprovado!")
    print("Certificado Ouro")