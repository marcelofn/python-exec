qtd_km_percorrido = float(input("Informe a quantidade de km rodados:"))
qtd_dias_alugado = int(input("Informe a quantidade de dias em que ficou alugado:"))

valor_diaria = 60.00
valor_km = 0.15

total = qtd_km_percorrido * valor_km + qtd_dias_alugado * valor_diaria

print("Total a pagar é: R$ %5.2f" % total)