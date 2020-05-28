maximo = int(input())
x = int(input())
op = input()
y = int(input())

if op == '+':
    result = x + y
elif op == '*':
    result = x * y

if result > maximo:
    print("OVERFLOW")
else:
    print("OK")