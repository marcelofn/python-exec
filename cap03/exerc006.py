salario = float(input("Qual o salário?"))
aumento = float(input("Qual o porcentagem do aumento?"))

valor_aumento = salario * aumento / 100
novo_salario = salario + valor_aumento

print("Você recebeu um aumento de R$ %5.2f, totalizando um valor de R$ %5.2f" %(valor_aumento, novo_salario))
