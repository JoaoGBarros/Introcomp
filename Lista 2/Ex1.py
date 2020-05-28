receita = float(input())
despesas = float(input())


if receita >= despesas:
    dif = receita - despesas
    print("Lucro de R$ %.2f!" % dif)
else:
    dif = despesas - receita
    print("Prejuizo de R$ %.2f!" % dif)