n = int(input("Digite um numero: "))
x = int(input("Digite novamente um numero: "))
while x <= n:
    print("{} x {} = {}".format(x, n, n*x))
    x += 1
