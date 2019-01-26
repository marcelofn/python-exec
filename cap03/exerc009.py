print("***********************************************************")
print("********Conversão de Fahrenheit em Celsius*****************")
print("***********************************************************")

temperatura_celsius = float(input("Digite a temperatura em ºC:"))

temperatura_convertida = temperatura_celsius * 9/5 + 32

print("A temperatura %5.2f°C em Fahrenheit é: %5.2f°F" % (temperatura_celsius, temperatura_convertida))