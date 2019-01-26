valor_mercadoria = float(input("Qual o valor da mercadoria?"))
desconto = float(input("Qual o percentual de desconto?"))

valor_desconto = valor_mercadoria * desconto / 100
novo_valor = valor_mercadoria - valor_desconto

print("O valor da mercadoria com desconto de %7.2f ficou por R$%5.2f" %(valor_desconto, novo_valor))