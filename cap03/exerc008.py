distancia = float(input("Qual a distancia em km?"))
vel_media = int(input("Qual a velocidade média em km/h?"))

tempo = distancia / vel_media
print("Você levará %5.2f horas para percorrer %7.0f km" %(tempo, distancia))