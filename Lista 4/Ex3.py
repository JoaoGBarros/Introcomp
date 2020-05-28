dic = {}
maior = 0

while True:
    aluno = input()
    if aluno == 'oooo':
        break
    else:
        nome, note = aluno.split()
        nota = float(note)
        dic[nome] = nota

for nota in dic.values():
    if nota > maior:
        maior = nota

for nome, nota in dic.items():
    if nota == maior:
        print(nome)
