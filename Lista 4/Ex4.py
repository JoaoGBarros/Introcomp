alunos = []
n = int(input())

for i in range(n):
    dados = input()
    nome, idade, CRN = dados.split()
    idade = str(int(float(idade)))
    CRN = str(float(CRN))
    tupla = (idade, nome, CRN)
    alunos.append(tupla)

for item in alunos:
    oficial = ' '.join(item)
    print(oficial)





